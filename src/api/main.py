"""VoiceChef FastAPI backend — port 8002."""
import json
import logging
import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# ---------------------------------------------------------------------------
# logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
)
log = logging.getLogger("voicechef")

# ---------------------------------------------------------------------------
# app
# ---------------------------------------------------------------------------
app = FastAPI(
    title="VoiceChef API",
    description="Converts voice notes about ingredients into three recipe options with sustainability scores.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# lazy model loading — avoids import at startup / in CI
# ---------------------------------------------------------------------------
_whisper_model = None


def _get_whisper():
    global _whisper_model
    if _whisper_model is None:
        log.info("Loading Whisper model (first call)…")
        from faster_whisper import WhisperModel
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _whisper_model = WhisperModel("small", device=device, compute_type="int8")
        log.info("Whisper ready on %s", device)
    return _whisper_model


# ---------------------------------------------------------------------------
# data loading
# ---------------------------------------------------------------------------
from config import (
    APP_VERSION,
    AVERAGE_RECIPE_CARBON_KG,
    CARBON_DB_PATH,
    NUTRITION_DB_PATH,
    WHISPER_MODEL,
)

with open(CARBON_DB_PATH) as f:
    CARBON_DB: dict = json.load(f)
with open(NUTRITION_DB_PATH) as f:
    NUTRITION_DB: dict = json.load(f)

# ---------------------------------------------------------------------------
# processing imports
# ---------------------------------------------------------------------------
from src.processing.extract import extract_ingredients_advanced, get_ingredient_emojis
from src.processing.recipe import generate_three_recipes


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _sustainability(ingredients: list[str]) -> dict:
    total_calories = total_protein = total_carbs = total_fat = total_carbon = 0.0
    carbon_per_ingredient: dict = {}

    for ing in ingredients:
        if ing in NUTRITION_DB:
            n = NUTRITION_DB[ing]
            total_calories += n.get("calories_per_100g", 0)
            total_protein += n.get("protein", 0)
            total_carbs += n.get("carbs", 0)
            total_fat += n.get("fat", 0)
        if ing in CARBON_DB:
            carbon = round(CARBON_DB[ing]["co2_kg_per_kg"] / 10, 4)
            total_carbon += carbon
            carbon_per_ingredient[ing] = carbon

    carbon_score = round(total_carbon, 3)
    carbon_saved = max(0, round(AVERAGE_RECIPE_CARBON_KG - carbon_score, 3))

    if carbon_score < 1.0:
        rating = "Excellent"
    elif carbon_score < 2.0:
        rating = "Good"
    elif carbon_score < 3.0:
        rating = "Fair"
    else:
        rating = "Needs Improvement"

    return {
        "total_carbon_kg_co2": carbon_score,
        "average_recipe_carbon_kg_co2": AVERAGE_RECIPE_CARBON_KG,
        "carbon_saved_kg_co2": carbon_saved,
        "sustainability_rating": rating,
        "carbon_per_ingredient": carbon_per_ingredient,
        "nutrition": {
            "total_calories": round(total_calories, 1),
            "protein_g": round(total_protein, 1),
            "carbs_g": round(total_carbs, 1),
            "fat_g": round(total_fat, 1),
        },
    }


def _build_response(text: str, ingredients: list[str]) -> dict:
    recipes = generate_three_recipes(ingredients)
    sustainability = _sustainability(ingredients)
    ingredient_emojis = get_ingredient_emojis(ingredients)

    return {
        "original_text": text,
        "extracted_ingredients": ingredients,
        "ingredient_emojis": ingredient_emojis,
        "recipes": recipes,
        "sustainability": sustainability,
    }


# ---------------------------------------------------------------------------
# endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": APP_VERSION,
        "whisper_model": WHISPER_MODEL,
    }


@app.post("/process-voice")
async def process_voice(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Please upload an audio file.")

    try:
        whisper = _get_whisper()
        segments, _ = whisper.transcribe(file.file, beam_size=5)
        full_text = "".join(seg.text for seg in segments).strip()
    except Exception as e:
        log.exception("Transcription failed")
        raise HTTPException(status_code=500, detail=f"Transcription error: {e}")

    if not full_text:
        raise HTTPException(status_code=400, detail="No speech detected in the audio file.")

    ingredients = extract_ingredients_advanced(full_text)
    if not ingredients:
        raise HTTPException(
            status_code=400,
            detail="No recognisable ingredients found. Try mentioning specific ingredients like 'chicken, tomatoes, rice'.",
        )

    return _build_response(full_text, ingredients)


_SAMPLE_TEXT = "I have chicken breast, tomatoes, rice, and garlic"
_SAMPLE_INGREDIENTS: Optional[list] = None


@app.get("/sample")
async def sample():
    global _SAMPLE_INGREDIENTS
    if _SAMPLE_INGREDIENTS is None:
        _SAMPLE_INGREDIENTS = extract_ingredients_advanced(_SAMPLE_TEXT)
    return _build_response(_SAMPLE_TEXT, _SAMPLE_INGREDIENTS)


@app.get("/ingredients")
async def list_ingredients():
    return {
        ing: {
            "carbon_kg_per_kg": CARBON_DB[ing]["co2_kg_per_kg"],
            "nutrition": NUTRITION_DB.get(ing, {}),
        }
        for ing in CARBON_DB
    }

# Voice-to-Recipe

Say what's in your fridge and get three recipe options (healthy, comfort, quick), each with a carbon-footprint score and a nutrition breakdown.

`🎤 voice → Whisper transcription → ingredient extraction → recipe matching → CO₂ + nutrition scoring → React UI`

## How it works

| Stage | Implementation |
|---|---|
| Speech-to-text | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) `small` model (int8; uses GPU if available), loaded lazily on first request |
| Ingredient extraction | Three-layer matcher (`src/processing/extract.py`): synonym map with 157 entries → direct match → partial match |
| Recipes | Curated recipe templates across 15 cuisines (`src/processing/recipe.py`); three options are returned per query |
| Sustainability | Per-ingredient CO₂e from `carbon_db.json` (76 ingredients, based on Poore & Nemecek 2018), compared with an average recipe |
| Nutrition | Calories, protein, carbs and fat from `nutrition_db.json` (76 ingredients, USDA-based) |
| Frontend | React + TypeScript + Vite + Tailwind; records with the browser MediaRecorder API |

## Run it

```bash
# backend
pip install -r requirements.txt
uvicorn src.api.main:app --reload --port 8000     # API docs at http://localhost:8000/docs

# frontend (in a second terminal)
cd frontend && npm install && npm run dev
```

The frontend runs on http://localhost:5175. No API keys are needed, because everything runs locally.

### API

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/process-voice` | Audio file → transcript, ingredients, recipes, CO₂ and nutrition |
| `GET` | `/sample` | Example response without recording |
| `GET` | `/ingredients` | Ingredients the matcher recognises |
| `GET` | `/health` | Liveness check |

## Tests

```bash
pytest          # tests/: API, extraction and recipe logic
```

## Layout

```
src/api/            FastAPI app
src/processing/     extract.py (ingredients), recipe.py (recipe templates)
frontend/           React + TypeScript UI
*_db.json           carbon, nutrition and ingredient-synonym data
tests/              pytest suite
```

## Limitations and next steps

- Recipes come from templates, not a generative model. Swapping in an LLM or a recipe API would widen coverage, at the cost of reproducibility.
- The carbon figures are per-ingredient averages and don't account for quantities or sourcing.
- Next: dietary filters, ingredient substitutions, and multi-language speech input (Whisper already supports it).

"""Ingredient extraction from free text."""
import json
import re
from typing import List

from config import CARBON_DB_PATH, INGREDIENT_MAP_PATH

with open(CARBON_DB_PATH) as f:
    CARBON_DB: dict = json.load(f)
with open(INGREDIENT_MAP_PATH) as f:
    INGREDIENT_MAP: dict = json.load(f)

# Canonical ingredient set
_CANONICAL: set = set(CARBON_DB.keys())


def _dedup(ingredients: List[str]) -> List[str]:
    """Remove items that are strict substrings of another item in the list."""
    result = []
    for ing in ingredients:
        if not any(ing != other and ing in other for other in ingredients):
            result.append(ing)
    return result


def extract_ingredients_advanced(text: str) -> List[str]:
    """3-layer ingredient extraction: synonym map → direct match → partial match."""
    text = text.lower()
    found: set = set()

    # Layer 1: synonym map
    for alias, canonical in INGREDIENT_MAP.items():
        if alias in text and canonical in _CANONICAL:
            found.add(canonical)

    # Layer 2: direct match against carbon DB keys
    for ingredient in _CANONICAL:
        if ingredient in text:
            found.add(ingredient)

    # Layer 3: partial word match (skip very short words)
    words = re.findall(r"\b\w+\b", text)
    for word in words:
        if len(word) > 3:
            for ingredient in _CANONICAL:
                if word in ingredient or ingredient in word:
                    found.add(ingredient)

    return _dedup(sorted(found))


INGREDIENT_EMOJIS: dict = {
    "chicken": "🍗", "beef": "🥩", "pork": "🥓", "lamb": "🐑",
    "salmon": "🐟", "tuna": "🐠", "fish": "🐟", "shrimp": "🦐",
    "egg": "🥚", "eggs": "🥚", "milk": "🥛", "cheese": "🧀",
    "butter": "🧈", "yogurt": "🥛", "cream": "🥛",
    "tomato": "🍅", "onion": "🧅", "garlic": "🧄", "carrot": "🥕",
    "broccoli": "🥦", "spinach": "🥬", "lettuce": "🥬",
    "cucumber": "🥒", "pepper": "🫑", "mushroom": "🍄",
    "potato": "🥔", "sweet potato": "🍠", "corn": "🌽",
    "avocado": "🥑", "lemon": "🍋", "lime": "🍋",
    "apple": "🍎", "banana": "🍌", "strawberry": "🍓",
    "rice": "🍚", "pasta": "🍝", "bread": "🍞",
    "noodle": "🍜", "noodles": "🍜", "quinoa": "🌾",
    "oats": "🌾", "flour": "🌾",
    "olive oil": "🫒", "oil": "🫙", "salt": "🧂",
    "ginger": "🫚", "curry": "🍛", "tofu": "🧊",
    "beans": "🫘", "lentil": "🫘", "chickpea": "🫘",
}


def get_ingredient_emojis(ingredients: List[str]) -> dict:
    return {ing: INGREDIENT_EMOJIS.get(ing, "🍽️") for ing in ingredients}

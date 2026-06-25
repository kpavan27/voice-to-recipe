"""VoiceChef configuration."""
from pathlib import Path

ROOT = Path(__file__).parent
DATA_DIR = ROOT  # JSON data files live at project root

CARBON_DB_PATH = DATA_DIR / "carbon_db.json"
NUTRITION_DB_PATH = DATA_DIR / "nutrition_db.json"
INGREDIENT_MAP_PATH = DATA_DIR / "ingredient_map.json"

API_HOST = "0.0.0.0"
API_PORT = 8002
APP_VERSION = "2.0.0"
WHISPER_MODEL = "small"
AVERAGE_RECIPE_CARBON_KG = 5.0

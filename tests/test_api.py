"""Tests for API endpoints (no Whisper required)."""
from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health_200():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_sample_200():
    response = client.get("/sample")
    assert response.status_code == 200
    data = response.json()
    assert "recipes" in data
    assert len(data["recipes"]) == 3
    assert "sustainability" in data
    assert "extracted_ingredients" in data


def test_sample_recipe_structure():
    response = client.get("/sample")
    assert response.status_code == 200
    recipes = response.json()["recipes"]
    badge_types = {r["badge_type"] for r in recipes}
    assert badge_types == {"healthy", "comfort", "quick"}


def test_process_voice_no_file_422():
    response = client.post("/process-voice")
    assert response.status_code == 422


def test_ingredients_endpoint():
    response = client.get("/ingredients")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0

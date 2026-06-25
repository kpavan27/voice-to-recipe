"""Tests for three-recipe generation."""
from src.processing.recipe import generate_three_recipes


def test_three_recipes_returned():
    recipes = generate_three_recipes(["chicken", "tomato", "rice"])
    assert len(recipes) == 3
    assert {r["badge_type"] for r in recipes} == {"healthy", "comfort", "quick"}


def test_recipe_structure():
    required_keys = [
        "title", "emoji", "badge", "badge_type", "description",
        "cooking_time", "servings", "difficulty", "health_rating",
        "health_label", "instructions", "pro_tips", "health_notes",
    ]
    for recipe in generate_three_recipes(["salmon", "broccoli"]):
        assert all(k in recipe for k in required_keys), (
            f"Missing keys in {recipe.get('title')}"
        )
        assert 1 <= recipe["health_rating"] <= 5
        assert len(recipe["instructions"]) >= 6
        for step in recipe["instructions"]:
            assert {"step", "title", "detail"} <= step.keys()
        assert isinstance(recipe["pro_tips"], list)
        assert len(recipe["pro_tips"]) >= 1
        assert "pros" in recipe["health_notes"]
        assert "cons" in recipe["health_notes"]


def test_recipe_order():
    recipes = generate_three_recipes(["chicken", "broccoli"])
    assert recipes[0]["badge_type"] == "healthy"
    assert recipes[1]["badge_type"] == "comfort"
    assert recipes[2]["badge_type"] == "quick"


def test_vegetarian_path():
    recipes = generate_three_recipes(["broccoli", "rice"])
    # all three should resolve without errors
    assert len(recipes) == 3
    for r in recipes:
        assert r["title"]


def test_breakfast_path():
    recipes = generate_three_recipes(["milk", "oats"])
    assert len(recipes) == 3
    for r in recipes:
        assert r["emoji"]


def test_simple_path():
    recipes = generate_three_recipes(["salt"])
    assert len(recipes) == 3


def test_placeholders_resolved():
    """No unresolved {placeholder} should remain in recipe strings."""
    for ingredients in [
        ["chicken", "tomato", "rice"],
        ["broccoli", "pasta"],
        ["eggs", "oats"],
    ]:
        for recipe in generate_three_recipes(ingredients):
            title = recipe["title"]
            assert "{" not in title and "}" not in title, (
                f"Unresolved placeholder in title: {title}"
            )
            for step in recipe["instructions"]:
                assert "{" not in step["title"]

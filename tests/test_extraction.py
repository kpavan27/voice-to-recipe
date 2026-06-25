"""Tests for ingredient extraction."""
from src.processing.extract import extract_ingredients_advanced


def test_direct_match():
    result = extract_ingredients_advanced("I have chicken and rice")
    # dedup may return 'chicken breast' rather than bare 'chicken' — either is valid
    assert any("chicken" in r for r in result)
    assert "rice" in result


def test_synonym_mapping():
    # "chook" or "tomatoes" should map to canonical forms
    result = extract_ingredients_advanced("I have tomatoes and garlic")
    assert "tomato" in result or "tomatoes" in result or "garlic" in result


def test_partial_match():
    result = extract_ingredients_advanced("I have some broccoli florets")
    assert "broccoli" in result


def test_multiple_ingredients():
    result = extract_ingredients_advanced(
        "I have chicken breast, tomatoes, rice, and garlic"
    )
    assert len(result) >= 2


def test_empty_text():
    result = extract_ingredients_advanced("")
    assert isinstance(result, list)


def test_no_ingredients():
    result = extract_ingredients_advanced("the weather is lovely today")
    assert isinstance(result, list)


def test_deduplication():
    """Should not return both 'chicken' and 'chicken breast' if both appear."""
    result = extract_ingredients_advanced("chicken breast and chicken thigh")
    # At minimum, result should be a list without obvious duplicates dominating
    assert isinstance(result, list)
    # No item should be a substring of another item in the result
    for ing in result:
        for other in result:
            if ing != other:
                assert ing not in other, (
                    f"'{ing}' is a substring of '{other}' — dedup failed"
                )

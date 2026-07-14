from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Mark ingredients valid if one allowed dark ingredient is present."""
    lowered_ingredients = ingredients.lower()
    is_valid = any(
        ingredient in lowered_ingredients
        for ingredient in dark_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"

def validate_ingredients(ingredients: str) -> str:
    """Mark ingredients valid if one allowed light ingredient is present."""
    from .light_spellbook import light_spell_allowed_ingredients

    lowered_ingredients = ingredients.lower()
    is_valid = any(
        ingredient in lowered_ingredients
        for ingredient in light_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"

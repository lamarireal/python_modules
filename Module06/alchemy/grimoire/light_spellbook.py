from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return ingredients permitted in light spells."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a valid light spell or reject an invalid one."""
    validation = validate_ingredients(ingredients)
    action = (
        "Spell recorded"
        if validation.endswith(" - VALID")
        else "Spell rejected"
    )
    return f"{action}: {spell_name} ({validation})"

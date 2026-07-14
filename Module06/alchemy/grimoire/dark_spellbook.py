from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return ingredients permitted in dark spells."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a valid dark spell or reject an invalid one."""
    validation = validate_ingredients(ingredients)
    action = (
        "Spell recorded"
        if validation.endswith(" - VALID")
        else "Spell rejected"
    )
    return f"{action}: {spell_name} ({validation})"

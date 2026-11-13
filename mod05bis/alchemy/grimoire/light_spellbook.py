from . import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    is_valid = light_validator.validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        result = f"Spell NOT recorded: {spell_name} "
    else:
        result = f"Spell recorded: {spell_name} "

    return result + is_valid

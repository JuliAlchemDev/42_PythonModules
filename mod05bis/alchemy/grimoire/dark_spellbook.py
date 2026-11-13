from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    is_valid = validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        result = f"Spell NOT recorded: {spell_name} "
    else:
        result = f"Spell recorded: {spell_name} "

    return result + is_valid

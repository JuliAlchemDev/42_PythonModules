from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_list = ingredients.lower().replace(",", "").split(" ")
    is_valid = "INVALID"
    for ingredient in ingredients_list:
        if ingredient in allowed:
            is_valid = "VALID"
            break
    return (f"({ingredients}) - {is_valid})")

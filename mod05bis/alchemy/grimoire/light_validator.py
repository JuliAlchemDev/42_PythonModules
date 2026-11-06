from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    ingredients_list = ingredients.replace(",", "").split(" ")
    is_valid = "INVALID"
    for ingredient in ingredients_list:
        if ingredient.lower() in allowed:
            is_valid = "VALID"
            break

    return (f"({ingredients} - {is_valid})")

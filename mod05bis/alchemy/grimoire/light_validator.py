def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ingredients_list = ingredients.lower().replace(",", " ").split(" ")
    is_valid = "INVALID"
    for ingredient in ingredients_list:
        if ingredient in allowed:
            is_valid = "VALID"
            break

    return (f"({ingredients} - {is_valid})")

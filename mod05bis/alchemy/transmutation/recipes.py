import elements as root_els
from .. import elements as pkg_els
from .. import potions


def lead_to_gold() -> str:
    air_el = pkg_els.create_air()
    fire_el = root_els.create_fire()
    strength = potions.strength_potion()

    return (f"Recipe transmuting Lead to Gold: "
            f"brew '{air_el}' and '{strength}' "
            f"mixed with '{fire_el}'")

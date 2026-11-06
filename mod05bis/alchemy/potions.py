import elements as root_els
from . import elements as pkg_els


def healing_potion() -> str:
    earth_el = pkg_els.create_earth()
    air_el = pkg_els.create_air()

    return f"Healing potion brewed with '{earth_el}' and '{air_el}'"


def strength_potion() -> str:
    fire_el = root_els.create_fire()
    water_el = root_els.create_water()

    return f"Strength potion brewed with '{fire_el}' and '{water_el}'"

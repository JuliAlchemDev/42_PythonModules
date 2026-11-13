import alchemy.grimoire.light_spellbook


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:", end=" ")

    print(alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire"))
    # INVALID SPELL TEST
    # print("Testing record light spell:", end=" ")
    # print(alchemy.grimoire.light_spellbook.light_spell_record(
    #     "Zombies", "Human Flesh, dirt and frogs"))


if __name__ == "__main__":
    main()

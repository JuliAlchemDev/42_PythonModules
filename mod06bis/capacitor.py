from ex3 import TransformCreatureFactory


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print(" base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


if __name__ == "__main__":
    main()

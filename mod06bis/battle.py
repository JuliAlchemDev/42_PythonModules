import ex3


def test_factory(factory: ex3.CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def base_fight(
    factory_1: ex3.CreatureFactory,
    factory_2: ex3.CreatureFactory
) -> None:

    f1_base_creature = factory_1.create_base()
    f2_base_creature = factory_2.create_base()
    print("Testing battle")
    print(f1_base_creature.describe())
    print(" vs.")
    print(f2_base_creature.describe())
    print(" fight!")
    print(f1_base_creature.attack())
    print(f2_base_creature.attack())


def main() -> None:
    factory_1 = ex3.FlameFactory()
    factory_2 = ex3.TransformCreatureFactory()

    test_factory(factory_1)
    test_factory(factory_2)

    base_fight(factory_1, factory_2)


if __name__ == "__main__":
    main()

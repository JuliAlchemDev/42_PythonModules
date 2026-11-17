import ex3
from ex3.creatures import Creature
import ex4


def battle(
        opponents: list[tuple[ex3.CreatureFactory,
                              ex4.BattleStrategy]]) -> None:

    fighters: list[tuple[Creature, ex4.BattleStrategy]] = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                creature_1, strategy_1 = fighters[i]
                creature_2, strategy_2 = fighters[j]

                print("\n* Battle *")
                print(creature_1.describe())
                print(" vs.")
                print(creature_2.describe())
                print(" now fight!")
                print(strategy_1.act(creature_1))
                print(strategy_2.act(creature_2))
    except ex4.StrategyError as error:
        print(error)


def main() -> None:
    opponents: list[tuple[ex3.CreatureFactory, ex4.BattleStrategy]] = []
    presentation: list[str] = []

    print("Tournament 0 (basic)")
    factory_1 = ex3.FlameFactory()
    strategy_1 = ex4.NormalStrategy()
    opponents.append((factory_1, strategy_1))

    factory_2 = ex3.TransformCreatureFactory()
    strategy_2 = ex4.AggressiveStrategy()
    opponents.append((factory_2, strategy_2))

    for factory, strategy in opponents:
        creature = factory.create_base()
        presentation.append(
            f"({creature.__class__.__name__}"
            f"+{strategy.__class__.__name__.replace('Strategy', '')})")

    joined = ", ".join(presentation)
    print(f" [ {joined} ]")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)

    opponents.clear()
    presentation.clear()
    print("\nTournament 1 (error)")
    factory_3 = ex3.TransformCreatureFactory()
    strategy_3 = ex4.AggressiveStrategy()
    opponents.append((factory_3, strategy_3))
    factory_4 = ex3.FlameFactory()
    strategy_4 = ex4.AggressiveStrategy()
    opponents.append((factory_4, strategy_4))

    for factory, strategy in opponents:
        creature = factory.create_base()
        presentation.append(
            f"({creature.__class__.__name__}"
            f"+{strategy.__class__.__name__.replace('Strategy', '')})")
    joined = ", ".join(presentation)
    print(f" [ {joined} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)


if __name__ == "__main__":
    main()

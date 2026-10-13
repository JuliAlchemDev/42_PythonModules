import random

PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]
ACHIEVEMENTS = ['Crafting Genius', 'Strategist', 'World Savior',
                'Speed Runner', 'Survivor', 'Master Explorer',
                'Treasure Hunter', 'Unstoppable', 'First Steps',
                'Collector Supreme', 'Untouchable', 'Sharp Mind',
                'Boss Slayer']


def gen_player_achievements() -> set[str]:
    return set(random.choices
               (ACHIEVEMENTS,
                k=random.randint(1, len(ACHIEVEMENTS))))


def build_player_data() -> dict[str, set[str]]:
    data = {}

    for player in PLAYERS:
        data[player] = gen_player_achievements()
    return data


def main() -> None:
    print("=== Achievement Tracker System ===", "\n")
    data = build_player_data()
    for player, achievements_set in data.items():
        print(f"Player {player}: {achievements_set}")

# All distinct achievements:
    all_achievements: set[str] = set()
    for achievements_set in data.values():
        all_achievements = all_achievements.union(achievements_set)
    print(f"\nAll distinct achievements: {all_achievements}\n")


# Common achievements:
    common_achs: set[str] = set(list(data.values())[0])
    for ach_set in data.values():
        common_achs = common_achs.intersection(ach_set)
    print(f"Common achievements: {common_achs}")
    print()
# Unique achievements:
    for player, achs_set in data.items():
        base = achs_set
        other_achs: set[str] = set()
        for name, achs in data.items():
            if player != name:
                other_achs = other_achs.union(achs)
        uniques = base.difference(other_achs)
        print(f"Only {player} has: {uniques}")
    print()
# Missing:
    for player, achievements_set in data.items():
        print(f"{player} is missing: {
            set(ACHIEVEMENTS).difference(achievements_set)}")


if __name__ == "__main__":
    main()

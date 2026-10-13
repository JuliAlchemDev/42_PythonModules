import random
PLAYERS = ['Alice', 'bob', 'Charlie',
           'dylan', 'Emma', 'Gregory',
           'john', 'kevin', 'Liam']


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_list = [player for player in PLAYERS]
    print(f"Initial list of players: {initial_list}")

    capitalized = [player.capitalize() for player in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")

    cap_only = [player for player in PLAYERS if player == player.capitalize()]
    print(f"New list of capitalized names only: {cap_only}")

    put_scores = {player: random.randint(0, 1000)
                  for player in capitalized
                  }
    print(f"Score dict: {put_scores}")

    avg = round(sum(put_scores.values()) / len(put_scores), 2)
    print(f"Score average is {avg}")

    avg_high = {player: score for player, score
                in put_scores.items() if score > avg}

    print(f"High scores: {avg_high}")


if __name__ == "__main__":
    main()

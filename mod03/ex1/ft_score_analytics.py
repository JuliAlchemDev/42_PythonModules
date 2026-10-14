import sys


def validate_scores(args: list[str]) -> list[int]:
    scores = []
    for arg in args:
        try:
            scores.append(int(arg))

        except ValueError:
            print(f"Invalid parameter: '{arg}'")
            # continue
    return scores


def main() -> None:
    args = sys.argv
    print("=== Player Score Analytics ===")
    scores = validate_scores(args[1:])

    if len(scores) == 0:
        print("No scores provided. ", end="")
        print(f"Usage: python3 {args[0]} <score1> <score2> ...")
    else:
        count_players = len(scores)
        total = sum(scores)
        avg = total / count_players
        highest = max(scores)
        lowest = min(scores)
        scr_range = highest - lowest

        print(f"Scores processed: {scores}")
        print(f"Total players: {count_players}")
        print(f"Total score: {total}")
        print(f"Average score: {avg}")
        print(f"High score: {highest}")
        print(f"Low score: {lowest}")
        print(f"Score range: {scr_range}")


if __name__ == "__main__":
    main()

import sys


def main() -> None:
    print("=== Command Quest ===")

    args = sys.argv
    args_count = len(args)
    print(f"Program name: {args[0]}")

    if args_count <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args_count - 1}")
        for i in range(1, args_count):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {args_count}")


if __name__ == "__main__":
    main()

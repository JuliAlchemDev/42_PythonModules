import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(alchemy.create_air())


if __name__ == "__main__":
    main()

    print(
        "Now show that not all functions can be reached\n"
        "This will raise an exception!")

    print("Testing the hidden create_earth:", end=" ")
    print(alchemy.create_earth())

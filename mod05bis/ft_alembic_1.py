import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(alchemy.create_air())


if __name__ == "__main__":
    main()

    # Outside main() on purpose: keeps the traceback to a single frame,
    # matching the expected output of the subject.
    print(
        "Now show that not all functions can be reached\n"
        "This will raise an exception!")

    print("Testing the hidden create_earth:", end=" ")
    print(alchemy.create_earth())

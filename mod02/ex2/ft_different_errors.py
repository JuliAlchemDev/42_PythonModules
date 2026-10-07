def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "5" + 5         # type: ignore
    return


def test_error_types() -> None:
    ops = [0, 1, 2, 3, 4]

    for op in ops:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            print("Operation completed successfully", "\n")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()

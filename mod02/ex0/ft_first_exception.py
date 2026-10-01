def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    data_list = ["25", "abc"]
    for data in data_list:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C", "\n")

        except ValueError as error:
            print(f"Caught input_temperature error: {error}", "\n")


def main() -> None:
    print(
        "=== Garden Temperature ===",
        "\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

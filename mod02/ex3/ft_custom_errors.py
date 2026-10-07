class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown water error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


def test_custom_errors() -> None:
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()

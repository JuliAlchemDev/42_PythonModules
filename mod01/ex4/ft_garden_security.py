class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

        else:
            self._height = value
            print(f"Height updated: {self.get_height():g}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self.get_age()} days")

    def show(self) -> None:
        print(f'{self.name}: {self._height}cm, {self._age} days old')


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("rose", 15.0, 10)
    print("Plant created: ", end='')
    plant1.show()
    print("")

    plant1.set_height(25.0)
    plant1.set_age(30)
    print("")

    plant1.set_height(-25.0)
    plant1.set_age(-30)
    print("")

    print("Current state: ", end='')
    plant1.show()


if __name__ == "__main__":
    main()

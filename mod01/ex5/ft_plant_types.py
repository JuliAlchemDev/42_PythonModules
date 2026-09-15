class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        if self.name == "Tomato":
            self.height += 2.1
        self.height = round(self.height, 1)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str
            ) -> None:
        super().__init__(name, height, age_days)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm",
            f"long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5


def main() -> None:
    print("=== Garden Plant Types ===")

    plant1 = Flower("rose", 15.0, 10, "red")
    print("=== Flower")
    plant1.show()
    print(" Rose has not bloomed yet")
    print("[asking the rose to bloom]")
    plant1.show()
    plant1.bloom()
    print("")

    plant2 = Tree("oak", 200.0, 365, 5.0)
    print("=== Tree")
    plant2.show()
    print("[asking the oak to produce shade]")
    plant2.produce_shade()
    print("")

    plant3 = Vegetable("tomato", 5.0, 10, "april")
    print("=== Vegetable")
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(0, 20):
        plant3.age()
        plant3.grow()
    plant3.show()


if __name__ == "__main__":
    main()

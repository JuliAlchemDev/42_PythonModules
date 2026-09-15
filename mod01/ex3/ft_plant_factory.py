class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age_days} days old')

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        if (self.name == "Rose"):
            self.height += 0.8
        elif (self.name == "Sunflower"):
            self.height += 1.4
        elif (self.name == "Cactus"):
            self.height += 0.2

        self.height = round(self.height, 1)


def main() -> None:
    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()

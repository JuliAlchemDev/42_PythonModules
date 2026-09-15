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
    print("=== Garden Plant Growth ===")

    plant1 = Plant("rose", 25, 30)
    # plant1 = GrowingPlant("sunflower", 80, 45)
    # plant1 = GrowingPlant("cactus", 15, 120)

    initial_height = plant1.height
    plant1.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.age()
        plant1.grow()
        plant1.show()

    total_growth = round((plant1.height - initial_height), 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()

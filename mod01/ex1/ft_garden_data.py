class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age_days} days old')


def main() -> None:
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120)
        ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()

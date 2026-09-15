class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age_days
        self.stats = Plant.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        self.stats.increase_stat("show")

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stats.increase_stat("grow")

    def age(self, amount: int) -> None:
        self.age_days += amount
        self.stats.increase_stat("age")

    def display_stats(self) -> None:
        self.stats.display_stats(False)

    @staticmethod
    def check_days(day: int) -> None:
        print(f"Is {day} days more than a year? -> ", end="")
        if day > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self._show_count = 0
            self._grow_count = 0
            self._age_count = 0
            self._shade_count = 0

        def increase_stat(self, stat: str) -> None:
            if stat == "show":
                self._show_count += 1
            elif stat == "grow":
                self._grow_count += 1
            elif stat == "age":
                self._age_count += 1
            elif stat == "shade":
                self._shade_count += 1

        def display_stats(self, has_shade: bool) -> None:
            if has_shade:
                print(
                    f"Stats: {self._grow_count} grow,",
                    f"{self._age_count} age, {self._show_count} show"
                    f"\n{self._shade_count} shade"
                    )
            else:
                print(
                    f"Stats: {self._grow_count} grow,",
                    f"{self._age_count} age, {self._show_count} show")


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

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.increase_stat("shade")
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long",
            f"and {self.trunk_diameter}cm wide."
            )

    def display_stats(self) -> None:
        self.stats.display_stats(True)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.is_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloomed is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def grow(self, amount: float = 0.0) -> None:
        if self.name == "Rose":
            amount = 8.0
        elif self.name == "Sunflower":
            amount = 30.0
        super().grow(amount)

    def bloom(self) -> None:
        self.is_bloomed = True


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            color: str
            ) -> None:
        super().__init__(name, height, age_days, color)

        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_days(30)
    Plant.check_days(400)
    print("")

    print("=== Flower")
    plant1 = Flower("rose", 15.0, 10, "red")
    plant1.show()
    show_stats(plant1)
    print("[asking the rose to grow and bloom]")
    plant1.grow()
    plant1.bloom()
    plant1.show()
    show_stats(plant1)
    print("")

    print("=== Tree")
    plant3 = Tree("oak", 200.0, 365, 5.0)
    plant3.show()
    show_stats(plant3)

    print("[asking the oak to produce shade]")
    plant3.produce_shade()
    show_stats(plant3)

    print("")

    print("=== Seed")
    plant2 = Seed("sunflower", 80.0, 45, "yellow")
    plant2.show()

    print("[make sunflower grow, age and bloom]")
    plant2.bloom()
    plant2.grow()
    plant2.age(20)
    plant2.show()
    show_stats(plant2)

    print("")

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    show_stats(anonymous)


if __name__ == "__main__":
    main()

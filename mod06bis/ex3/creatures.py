from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, type):
        self.name = name
        self.creature_type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return f"{self.name} uses Flamethrower!"

from abc import ABC, abstractmethod
from .creatures import Creature


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


#  TODO: how to know all abstract methods needed??????

class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def attack(self):
        return f"{self.name} attacks normally."

    def transform(self):
        pass

    def revert(self):
        pass


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self):
        return f"{self.name} attacks normally."

    def transform(self):
        pass

    def revert(self):
        pass

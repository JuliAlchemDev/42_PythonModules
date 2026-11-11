from abc import ABC, abstractmethod

from .creatures import Flameling, Pyrodon
from .capabilities import Shiftling, Morphagon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()


def main():
    # python3 -m ex3.factories
    print("Hello World!")


if __name__ == "__main__":
    main()

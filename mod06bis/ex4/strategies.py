from abc import ABC, abstractmethod
from ex3.creatures import Creature
from ex3.capabilities import TransformCapability
from typing import cast


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, entity: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, entity: Creature) -> str:
        return entity.attack()

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, entity: Creature) -> str:
        if self.is_valid(entity):
            transformer = cast(TransformCapability, entity)
            action = f"{transformer.transform()}\n" \
                f"{entity.attack()}\n" \
                f"{transformer.revert()}"

            return action
        else:
            raise StrategyError("Battle error, aborting tournament: "
                                f"Invalid Creature '{entity.name}'"
                                " for this aggressive strategy"
                                )

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

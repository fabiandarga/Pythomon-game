from random import choice
from typing import Type

from game.objects.Pythomon import Pythomon
from game.objects.pythomon.iffy import Iffy
from game.objects.pythomon.loopard import Loopard
from game.objects.pythomon.nullbear import Nullbear


class PythomonFactory:
    def __init__(self, monsters: list[Type[Pythomon]]) -> None:
        self._monsters = monsters

    def generate_random(self) -> Pythomon:
        base_class = choice(self._monsters)
        monster = base_class()
        # Maybe changing some factors randomly
        return monster

pythomon_factory = PythomonFactory([Iffy, Loopard, Nullbear])
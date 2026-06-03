from random import choice
from typing import Type

from game.objects.Pythomon import Pythomon
from game.objects.pythomon.IfMon import IfMon
from game.objects.pythomon.LoopMon import LoopMon


class PythomonFactory:
    def __init__(self, monsters: list[Type[Pythomon]]) -> None:
        self._monsters = monsters

    def generate_random(self) -> Pythomon:
        base_class = choice(self._monsters)
        monster = base_class()
        # Maybe changing some factors randomly
        return monster

pythomon_factory = PythomonFactory([IfMon, LoopMon])
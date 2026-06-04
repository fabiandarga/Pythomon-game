from dataclasses import dataclass
from game.objects.Attack import Attack
from game.AttackResult import AttackResult

class Nullpointer(Attack):
    name: str = "Nullpointer"
    damage: int = 20


NULLPOINTER = Nullpointer()
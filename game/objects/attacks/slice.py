from game.objects.Attack import Attack
from dataclasses import dataclass

@dataclass(frozen=True)
class Slice(Attack):
    name: str = "Slice"
    damage: int = 15

SLICE = Slice()
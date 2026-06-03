from os import name

from game.AttackResult import AttackResult
from game.objects.Attack import Attack

MAX_ATTACK_OPTIONS = 4

class Pythomon:

    def __init__(self) -> None:
        self._name = ""
        self._hp = 0
        self._attacks: list[Attack] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, hp: int) -> None:
        self._hp = hp

    def reduce_hp(self, amount: int):
        self._hp -= amount

    @property
    def attacks(self) -> list[Attack]:
        return self._attacks

    def add_attack(self, attack: Attack):
        if len(self.attacks) < 4:
            self._attacks.append(attack)

    def attack(self, index: int, other: Pythomon) -> AttackResult:
        attack = self.attacks[index]
        return attack.execute(self, other)
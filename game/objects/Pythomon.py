from game.objects.status import Status


from game.AttackResult import AttackResult
from game.objects.Attack import Attack

MAX_ATTACK_OPTIONS = 4

class Pythomon:
    _name: str
    _base_hp: int = 0
    _initial_energy: int = 0
    _base_attacks: list[Attack] = []

    def __init__(self) -> None:
        self._hp = self._base_hp
        self._energy = self._initial_energy
        self._attacks = list(self._base_attacks)
        self._status = Status.NORMAL

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def energy(self) -> int:
        return self._energy

    def reduce_energy(self, amount: int):
        self._energy -= amount

    def reduce_hp(self, amount: int):
        self._hp -= amount

    @property
    def attacks(self) -> list[Attack]:
        return self._attacks

    def add_attack(self, attack: Attack):
        if len(self.attacks) < 4:
            self._attacks.append(attack)

    def change_status(self, status: Status) -> tuple[Status, Status]:
        old_status = self._status
        self._status = status
        return old_status, status

    @property
    def is_sleeping(self) -> bool:
        return self._status == Status.SLEEPING

    @property
    def is_confused(self) -> bool:
        return self._status == Status.CONFUSED

    @property
    def is_poisoned(self):
        return self._status == Status.POISONED
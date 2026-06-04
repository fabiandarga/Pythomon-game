from game.AttackResult import AttackResult
from typing import TYPE_CHECKING
from game.objects.status import StatusChangeResult

if TYPE_CHECKING:
    from game.objects.Pythomon import Pythomon

class Attack:
    _name: str
    _damage: int
    _cost: int

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    def execute(self, attacker: 'Pythomon', defender: 'Pythomon') -> AttackResult:
        dmg = self.calculate_damage()
        defender.reduce_hp(dmg)
        attacker.reduce_energy(self._cost)
        status_changes = self.apply_effects(attacker, defender)
        return AttackResult(self.name, dmg, defender.hp, status_changes)

    def apply_effects(self, attacker: 'Pythomon', defender: 'Pythomon') -> StatusChangeResult:
        return None, None

    def calculate_damage(self) -> int:
        return self._damage
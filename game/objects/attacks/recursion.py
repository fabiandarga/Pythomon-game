from dataclasses import dataclass
from game.objects.Attack import Attack
from game.objects.status import Status


@dataclass(frozen=True)
class Recursion(Attack):
    _name = "Recursion"
    _damage = 5
    _cost = 30

    def apply_effects(self, attacker, defender):
        def_change = defender.change_status(Status.POISONED)
        return None, def_change

RECURSION = Recursion()
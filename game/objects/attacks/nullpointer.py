from game.objects.Attack import Attack
from game.objects.status import Status

class Nullpointer(Attack):
    _name: str = "Nullpointer"
    _damage: int = 20
    _cost = 20

    def apply_effects(self, attacker, defender):
        attacker_change = attacker.change_status(Status.CONFUSED)
        defender_change = defender.change_status(Status.CONFUSED)
        return attacker_change, defender_change


NULLPOINTER = Nullpointer()
from game.objects.Attack import Attack
from game.objects.status import Status

class WakeUp(Attack):
    _name = "Wake Up"
    _damage = 0
    _cost = 50

    def apply_effects(self, attacker, defender):
        attacker_change = attacker.change_status(Status.NORMAL)
        return attacker_change, None

WAKE_UP = WakeUp()
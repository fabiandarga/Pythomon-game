from random import random

from game.objects.Attack import Attack
from game.objects.status import Status

class Wait(Attack):
    _name = "Wait"
    _damage = 0
    _cost = 0

    def apply_effects(self, attacker, defender):
        if random() <= 0.2:
            attacker_change = attacker.change_status(Status.NORMAL)
            return attacker_change, None
        return None, None

WAIT = Wait()
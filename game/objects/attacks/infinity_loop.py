from game.objects.Attack import Attack
from game.objects.status import Status

class InfinityLoop(Attack):
    _name: str = "Infinity Loop"
    _damage: int = 25
    _cost = 50

    def apply_effects(self, attacker, defender):
        defender_change = defender.change_status(Status.SLEEPING)
        return None, defender_change


INFINITY_LOOP = InfinityLoop()
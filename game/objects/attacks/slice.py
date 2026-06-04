import random
from game.objects.Attack import Attack

class Slice(Attack):
    _name = "Slice"
    _damage = 10
    _cost = 15


    def calculate_damage(self) -> int:
        extra_dmg = random.random() * self.damage
        return self.damage + int(extra_dmg)

SLICE = Slice()

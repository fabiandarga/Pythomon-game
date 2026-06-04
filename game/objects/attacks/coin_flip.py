import random
from game.objects.Attack import Attack

class CoinFlip(Attack):
    _name = "Coin Flip"
    _damage = 0
    _cost = 20

    def calculate_damage(self) -> int:
        return random.choice([0, 40])

COIN_FLIP = CoinFlip()
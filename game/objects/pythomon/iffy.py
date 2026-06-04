from game.objects.Pythomon import Pythomon
from game.objects.attacks import SCRATCH, COIN_FLIP, SLICE


class Iffy(Pythomon):
    _name = "Iffy"
    _base_hp = 70
    _base_attacks = [SCRATCH, SLICE, COIN_FLIP]

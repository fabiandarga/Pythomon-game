from game.objects.Pythomon import Pythomon
from game.objects.attacks import SCRATCH, TACKLE


class Iffy(Pythomon):
    _name = "Iffy"
    _base_hp = 70
    _base_attacks = [SCRATCH, TACKLE]

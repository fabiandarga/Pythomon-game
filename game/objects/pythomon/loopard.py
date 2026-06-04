from game.objects.Pythomon import Pythomon
from game.objects.attacks import SCRATCH, RECURSION, INFINITY_LOOP


class Loopard(Pythomon):
    _name = "Loopard"
    _base_hp = 100
    _base_attacks = [SCRATCH, RECURSION, INFINITY_LOOP]


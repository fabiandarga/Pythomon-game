from game.objects.Pythomon import Pythomon
from game.objects.attacks import TACKLE, INFINITY_LOOP


class Pythork(Pythomon):
    _name = "Pythork"
    _base_hp = 90
    _base_attacks = [TACKLE, INFINITY_LOOP]
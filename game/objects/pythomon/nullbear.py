from game.objects.Pythomon import Pythomon
from game.objects.attacks import SCRATCH, TACKLE, NULLPOINTER


class Nullbear(Pythomon):
    _name = "Nullbear"
    _base_hp = 120
    _initial_energy = 80
    _base_attacks = [SCRATCH, TACKLE, NULLPOINTER]


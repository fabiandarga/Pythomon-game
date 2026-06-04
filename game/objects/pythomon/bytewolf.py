from game.objects.Pythomon import Pythomon
from game.objects.attacks import SCRATCH, SLICE, NULLPOINTER


class Bytewolf(Pythomon):
    _name = "Bytewolf"
    _base_hp = 95
    _initial_energy = 100
    _base_attacks = [SCRATCH, SLICE, NULLPOINTER]
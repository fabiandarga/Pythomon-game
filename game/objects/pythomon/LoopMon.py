from game.objects.Pythomon import Pythomon
from game.objects.attacks.Scratch import Scratch
from game.objects.attacks.Tackle import Tackle


class LoopMon(Pythomon):
    def __init__(self):
        super().__init__()
        self._name = "LoopMon"
        self._hp = 100
        self.add_attack(Scratch())
        self.add_attack(Tackle())

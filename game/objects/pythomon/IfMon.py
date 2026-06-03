from game.objects.Pythomon import Pythomon
from game.objects.attacks.Scratch import Scratch
from game.objects.attacks.Tackle import Tackle


class IfMon(Pythomon):
    def __init__(self):
        Pythomon.__init__(self)
        self._name = "IfMon"
        self._hp = 70
        self.add_attack(Scratch())
        self.add_attack(Tackle())
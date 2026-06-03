from game.objects.Pythomon import Pythomon


class LoopMon(Pythomon):
    def __init__(self):
        super().__init__()
        self._name = "LoopMon"
        self._hp = 100
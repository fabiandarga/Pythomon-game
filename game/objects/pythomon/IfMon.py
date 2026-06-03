from game.objects.Pythomon import Pythomon


class IfMon(Pythomon):
    def __init__(self):
        Pythomon.__init__(self)
        self._name = "IfMon"
        self._hp = 70
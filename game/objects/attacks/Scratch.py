from game.objects.Attack import Attack


class Scratch(Attack):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Scratch"
        self._damage = 10
from game.objects.Attack import Attack


class Tackle(Attack):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Tackle"
        self._damage = 25
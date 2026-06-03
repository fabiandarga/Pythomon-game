from os import name


class Pythomon:

    def __init__(self) -> None:
        self._name = ""
        self._hp = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, hp: int) -> None:
        self._hp = hp
class Attack:
    def __init__(self):
        self._name = ""
        self._damage = 0

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage
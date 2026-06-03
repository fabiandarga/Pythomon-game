class Attack:
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage
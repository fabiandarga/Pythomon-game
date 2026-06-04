from game.AttackResult import AttackResult


class Attack:
    _name: str
    _damage: int

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    def execute(self, attacker: 'Pythomon', defender: 'Pythomon') -> AttackResult:
        damage = self.damage
        defender.reduce_hp(damage)
        return AttackResult(self.name, damage, defender.hp)
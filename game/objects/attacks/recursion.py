from dataclasses import dataclass
from game.objects.Attack import Attack
from game.AttackResult import AttackResult

@dataclass(frozen=True)
class Recursion(Attack):
    name: str = "Recursion"
    damage: int = 5

    def execute(self, attacker, defender) -> AttackResult:
        # Hits multiple times, but weaker each time
        total = 0
        dmg = self.damage
        for _ in range(4):
            defender.reduce_hp(dmg)
            total += dmg
            dmg //= 2
        return AttackResult(self.name, total, defender.hp)

RECURSION = Recursion()
import random
from dataclasses import dataclass
from game.objects.Attack import Attack
from game.AttackResult import AttackResult

@dataclass(frozen=True)
class IndentError(Attack):
    name: str = "Indent Error"
    damage: int = 30

    def execute(self, attacker, defender) -> AttackResult:
        # Confuses the defender — 30% chance to miss
        if random.random() < 0.3:
            return AttackResult(self.name, 0, defender.hp)
        defender.reduce_hp(self.damage)
        return AttackResult(self.name, self.damage, defender.hp)

INDENT_ERROR = IndentError()
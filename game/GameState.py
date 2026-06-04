from typing import Literal, Optional

from game.objects.Attack import Attack
from game.factories.PythomonFactory import pythomon_factory
from game.objects.Pythomon import Pythomon


class GameState:
    def __init__(self):
        self.player_monster: Optional[Pythomon] = None
        self.enemy_monster: Optional[Pythomon] = None
        self.active_player: Literal["player", "enemy"] = "player"
        self.running = True

    def assign_random_monsters(self):
        self.player_monster = pythomon_factory.generate_random()
        self.enemy_monster = pythomon_factory.generate_random()

    def execute_attack(self, attack: Attack):
        player = self.player_monster
        enemy = self.enemy_monster
        if self.active_player == "player":
            return attack.execute(player, enemy)
        else:
            return attack.execute(enemy, player)

    def toggle_active_player(self):
        self.active_player = "player" if self.active_player == "enemy" else "enemy"
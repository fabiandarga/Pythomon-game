import os
from typing import Optional

from game.AttackResult import AttackResult
from game.GameState import GameState
import readchar

class GameUI:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def print_state(self):
        print("--------------------")
        print("~Player Monster~")
        print(f"{self.game_state.player_monster.name}")
        print(f"HP: {self.game_state.player_monster.hp}")
        print("\n~Enemy Monster~")
        print(f"{self.game_state.enemy_monster.name}")
        print(f"HP: {self.game_state.enemy_monster.hp}")
        print("--------------------")

    def display_attack_choices(self):
        print("Was willst du tun?\n")
        attacks = self.game_state.player_monster.attacks
        for i, attack in enumerate(attacks):
            print(f"[{i+1}] {attack.name}")

    def wait_for_int_choice(self) -> int:
        while True:
            try:
                key = int(readchar.readkey())
                return key
            except ValueError:
                pass

    def wait_for_enter(self):
        while True:
            key = readchar.readkey()
            if key == readchar.key.ENTER:
                return


    def display_attack_result(self, result: AttackResult):
        gs = self.game_state
        player_monster = self.game_state.player_monster
        enemy_monster = self.game_state.enemy_monster

        print(f"\n\033[1m{result.attack_name}\033[0m")
        attacker_name = f"{player_monster.name} (Player)" if gs.active_player == "player" else f"{enemy_monster.name} (Enemy)"
        defender_name = f"{enemy_monster.name} (Enemy)" if gs.active_player == "player" else f"{player_monster.name} (Player)"
        print(f"{attacker_name} dealt {result.hp_lost} damage to {defender_name}.")
        if result.alive:
            print(f"{defender_name} has {result.remaining_hp} HP left.")
        else:
            print(f"{defender_name} is unconscious.")

    def clear_screen(self):
        print("\033[2J\033[H", end="", flush=True)


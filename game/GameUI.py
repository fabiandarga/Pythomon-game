from game.objects.Attack import Attack
from game.objects.Pythomon import Pythomon
from game.AttackResult import AttackResult
from game.GameState import GameState
import readchar

from game.objects.status import Status


class GameUI:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def print_state(self):
        print("--------------------")
        print("~Player Monster~")
        monster = self.game_state.player_monster
        print(f"{monster.name}")
        if monster._status != Status.NORMAL:
            print(f"<{self.get_status_text(monster._status)}>")
        print(f"HP: {monster.hp}")

        print("\n~Enemy Monster~")
        enemy_monster = self.game_state.enemy_monster
        print(f"{enemy_monster.name}")
        if enemy_monster._status is not Status.NORMAL:
            print(f"<{self.get_status_text(enemy_monster._status)}>")
        print(f"HP: {enemy_monster.hp}")
        print("--------------------")

    def get_status_text(self, status: Status) -> str:
        match status:
            case Status.POISONED:
                return "Vergiftet"
            case Status.CONFUSED:
                return "Verwirrt"
            case Status.SLEEPING:
                return "Schläft"
            case _:
                return "Gesund"

    def display_attack_choices(self, options: list[Attack]):
        print("Was willst du tun?\n")
        for i, option in enumerate(options):
            print(f"[{i+1}] {option.name}")

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

    def display_sleep(self, monster: Pythomon):
        print(f"ZZZzzz... {monster.name} is sleeping.")

    def display_poison_damage(self, monster: Pythomon, dmg: int):
        print(f"☠️ {monster.name} took {dmg} poison damage.")

    def clear_screen(self):
        print("\033[2J\033[H", end="", flush=True)


    def display_victory_screen(self):
        self.clear_screen()
        print("""
            . ★ . * . * . ★ . * .
        * . * . ★ . * . * . ★ . * . *
                🏆 You win! 🏆
           . ✦ . 🎆 . ✦ . 🎆 . ✦ .
            . ★ . * . * . ★ . * .
        """)

    def display_game_over_screen(self):
        self.clear_screen()
        print("""
        
        . . . . . . . . . . . .
        . . . . . . . . . . . .
           💀 You lose... 💀
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        """)
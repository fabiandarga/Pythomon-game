import random

from game.GameState import GameState
from game.GameUI import GameUI


class Game:
    def __init__(self):
        self.game_state = GameState()
        self.ui = GameUI(self.game_state)

    def start_new_game(self):
        self.game_state.assign_random_monsters()
        self.game_state.active_player = "player"

        while self.game_state.running:
            self.ui.clear_screen()
            self.ui.print_state()

            self.player_turn()
            print("[Press Enter]")
            self.ui.wait_for_enter()
            print("--------------")

            self.enemy_turn()
            print("[Press Enter]")
            self.ui.wait_for_enter()

    def player_turn(self):
        self.game_state.active_player = "player"
        print("Du bist am Zug!")
        self.ui.display_attack_choices()

        choice = self.ui.wait_for_int_choice()

        result = self.game_state.execute_attack(choice - 1)
        self.ui.display_attack_result(result)

        if not result.alive:
            self.game_state.running = False

    def enemy_turn(self):
        self.game_state.active_player = "enemy"
        print("Der gegner ist dran")
        monster = self.game_state.enemy_monster
        choice = random.randint(0, len(monster.attacks) - 1 )
        result = monster.attack(choice, self.game_state.player_monster)

        self.ui.display_attack_result(result)

        if not result.alive:
            self.game_state.running = False



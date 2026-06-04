import random

from game.objects.Attack import Attack
from game.objects.attacks.wait import WAIT
from game.objects.attacks.wake_up import WAKE_UP
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
            if not self.game_state.running:
                break

            print("--------------")
            self.enemy_turn()
            print("[Press Enter]")
            self.ui.wait_for_enter()

            self.game_state.player_monster.add_energy(10)
            self.game_state.enemy_monster.add_energy(10)

        if self.game_state.player_monster.hp <= 0:
            self.ui.display_game_over_screen()
        else:
            self.ui.display_victory_screen()

    def player_turn(self):
        print("Du bist am Zug!")
        self.game_state.active_player = "player"
        monster = self.game_state.player_monster

        choices = monster.attacks
        if monster.is_sleeping:
            self.ui.display_sleep(monster)
            choices = [WAIT, WAKE_UP]
        elif monster.is_poisoned:
            monster.reduce_hp(5)
            self.ui.display_poison_damage(monster, 5)
            if monster.hp <= 0:
                self.game_state.running = False
                return

        has_valid_choices = any(c.cost <= monster.energy for c in choices)
        if not has_valid_choices:
            choices = [WAIT]
        self.ui.display_attack_choices(choices, monster.energy)

        attack = None
        while attack is None:
            choice = self.ui.wait_for_int_choice(len(choices))
            attack = choices[choice - 1]
            if attack.cost > monster.energy:
                attack = None

        result = self.game_state.execute_attack(attack)
        self.ui.display_attack_result(result)

        if not result.alive:
            self.game_state.running = False

    def enemy_turn(self):
        print("Der gegner ist dran")
        self.game_state.active_player = "enemy"
        monster = self.game_state.enemy_monster

        choices = monster.attacks
        if monster.is_sleeping:
            self.ui.display_sleep(monster)
            choices = [WAIT, WAKE_UP]
        elif monster.is_poisoned:
            monster.reduce_hp(5)
            self.ui.display_poison_damage(monster, 5)
            if monster.hp <= 0:
                self.game_state.running = False
                return
        choices = [c for c in choices if c.cost <= monster.energy]
        if len(choices) == 0:
            choices = [WAIT]
        choice = random.randint(0, len(choices) - 1 )
        attack = choices[choice - 1]
        result = self.game_state.execute_attack(attack)
        self.ui.display_attack_result(result)

        if not result.alive:
            self.game_state.running = False



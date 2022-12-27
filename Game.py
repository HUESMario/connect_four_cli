from Player import Player
from Playground import Playground
from BColors import BColors


class Game:
    def __init__(self, playground, players):
        self.playground = playground
        self.players.append(players[0])
        self.players.append(players[1])

    def show_current_player(self):
        print(f"{self.players[self.active_player - 1].player_color}your Turn {self.players[self.active_player - 1].get_name()} ( {self.players[self.active_player - 1].get_char()} ){BColors.ENDC}")

    def switch_players(self):
        if self.active_player == 1:
            self.active_player = 2
        elif self.active_player == 2:
            self.active_player = 1

    def player_action(self):
        correct_input = False
        while not correct_input:
            try:
                player_input = int(input("enter your row (1-7): ")) - 1
                correct_input = True
            except ValueError:
                continue
        if not self.playground.add_player_chip(player_input, self.players[self.active_player - 1]):
            correct_input = False
            while not correct_input:
                try:
                    new_player_input = int(input("please enter an correct row, if you enter a wrong one again, it's the enemies turn: ")) - 1
                    correct_input = True
                except ValueError:
                    continue
            self.playground.add_player_chip(new_player_input, self.players[self.active_player - 1])

    def check_for_win(self):
        for i in range(len(self.playground.play_field) - 1):
            for j in range(len(self.playground.play_field[i]) - 1):
                if self.playground.play_field[i][j].is_used():
                    if not j + 3 > len(self.playground.play_field[i]) - 1:
                        if self.playground.play_field[i][j].get_char() == self.playground.play_field[i][j + 1].get_char() and self.playground.play_field[i][j + 1].get_char() == self.playground.play_field[i][j + 2].get_char() and self.playground.play_field[i][j + 2].get_char() == self.playground.play_field[i][j + 3].get_char():
                            if self.playground.play_field[i][j].get_char() == "X":
                                self.game_won = 1
                            elif self.playground.play_field[i][j].get_char() == "O":
                                self.game_won = 2
                            return True
                    if not i + 3 > len(self.playground.play_field) - 1:
                        if self.playground.play_field[i][j].get_char() == self.playground.play_field[i + 1][j].get_char() and self.playground.play_field[i + 1][j].get_char() == self.playground.play_field[i + 2][j].get_char() and self.playground.play_field[i + 2][j].get_char() == self.playground.play_field[i + 3][j].get_char():
                            if self.playground.play_field[i][j].get_char() == "X":
                                self.game_won = 1
                            elif self.playground.play_field[i][j].get_char() == "O":
                                self.game_won = 2
                            return True
                    if not i + 3 > len(self.playground.play_field) - 1 and not j + 3 > len(self.playground.play_field[i]) - 1:
                        if self.playground.play_field[i][j].get_char() == self.playground.play_field[i + 1][j + 1].get_char() and self.playground.play_field[i + 1][j + 1].get_char() == self.playground.play_field[i + 2][j + 2].get_char() and self.playground.play_field[i + 2][j + 2].get_char() == self.playground.play_field[i + 3][j + 3].get_char():
                            if self.playground.play_field[i][j].get_char() == "X":
                                self.game_won = 1
                            elif self.playground.play_field[i][j].get_char() == "O":
                                self.game_won = 2
                            return True
                    if not i + 3 > len(self.playground.play_field) - 1 and not j - 3 < 0:
                        if self.playground.play_field[i][j].get_char() == self.playground.play_field[i + 1][j - 1].get_char() and self.playground.play_field[i + 1][j - 1].get_char() == self.playground.play_field[i + 2][j - 2].get_char() and self.playground.play_field[i + 2][j - 2].get_char() == self.playground.play_field[i + 3][j - 3].get_char():
                            if self.playground.play_field[i][j].get_char() == "X":
                                self.game_won = 1
                            elif self.playground.play_field[i][j].get_char() == "O":
                                self.game_won = 2
                            return True
        return False

    def victory_screen(self):
        print(self.playground.show_play_field())
        print(f"Congratulations to you {self.players[self.game_won - 1].get_name()}")

    def prompt_restart(self):
        ask_restart = input("You want to restart?(Y/N): ")
        if not ask_restart == "N" and not ask_restart == "n":
            return True
        return False

    def play(self):
        while self.game_won == 0:
            self.show_current_player()
            self.playground.show_play_field()
            self.player_action()
            self.check_for_win()
            if self.game_won != 0:
                self.victory_screen()
                if self.prompt_restart():
                    del self.players[1]
                    del self.players[0]
                    del self.playground
                    player_1 = Player(1)
                    player_2 = Player(2)
                    playground = Playground()
                    new_game = Game(playground, [player_1, player_2])
                    new_game.play()
            self.switch_players()

    playground = []
    players = []
    active_player = 1
    game_won = 0

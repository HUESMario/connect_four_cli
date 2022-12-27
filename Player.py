from BColors import BColors


class Player:
    def __init__(self, which_player):
        self.player_name = input("Enter your Name Player {}: ".format(which_player))
        if which_player == 1:
            self.player_char = "X"
            self.player_color = BColors.WARNING
        elif which_player == 2:
            self.player_char = "O"
            self.player_color = BColors.FAIL

    def get_name(self):
        return self.player_name

    def get_char(self):
        return self.player_char

    def get_color(self):
        return self.player_color

    player_name = " "
    player_color = BColors.WARNING
    player_char = " "

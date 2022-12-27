from Dummy import Dummy
from BColors import  BColors


class Field:
    def __init__(self):
        self.data = Dummy()

    def get_name(self):
        return self.data.get_name()

    def get_char(self):
        return self.data.get_char()

    def get_color(self):
        return self.data.get_color()

    def set_data(self, player):
        self.is_in_use = True
        self.data = player

    def is_used(self):
        return self.is_in_use

    data = Dummy()
    is_in_use = False


class Playground:
    def __init__(self):
        self.play_field = []
        for i in range(6):
            field_arr = []
            for j in range(7):
                new_field = Field()
                field_arr.append(new_field)
            self.play_field.append(field_arr)

    def show_play_field(self):
        print(self.pf_color)
        print("-----------------------------")
        for i in range(5, -1, -1):
            print(
                f"| {self.play_field[i][0].get_color()}{self.play_field[i][0].get_char()}{self.pf_color} | {self.play_field[i][1].get_color()}{self.play_field[i][1].get_char()}{self.pf_color} | {self.play_field[i][2].get_color()}{self.play_field[i][2].get_char()}{self.pf_color} | {self.play_field[i][3].get_color()}{self.play_field[i][3].get_char()}{BColors.OKGREEN} | {self.play_field[i][4].get_color()}{self.play_field[i][4].get_char()}{BColors.OKGREEN} | {self.play_field[i][5].get_color()}{self.play_field[i][5].get_char()}{BColors.OKGREEN} | {self.play_field[i][6].get_color()}{self.play_field[i][6].get_char()}{BColors.OKGREEN} |")
        print("-----------------------------")
        print(BColors.ENDC)

    def add_player_chip(self, row, player):
        added_player = False
        if not row > len(self.play_field):
            for i in range(6):
                if self.play_field[i][row].is_used():
                    continue
                elif not self.play_field[i][row].is_used():
                    self.play_field[i][row].set_data(player)
                    added_player = True
                if added_player:
                    break
        return added_player

    play_field = []
    pf_color = BColors.OKGREEN

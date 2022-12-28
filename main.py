# Author: Mario Happle
# Version: 1.0.0
# Game Name: Connect_four_cli
# Written with: PyCharm Community Edition 2022.2.2


from Player import Player
from Playground import Playground
from Game import Game


def four_wins():
    player_1 = Player(1)
    player_2 = Player(2)
    playground = Playground()
    game = Game(playground, [player_1, player_2])
    game.play()


if __name__ == '__main__':
    four_wins()

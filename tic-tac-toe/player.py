import math
import random

class Player:
    def _init_(self, letter):
        # letter is x and o
        self.letter = letter

    # we want all players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
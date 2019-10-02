from flask import Flask


class Game:
    def __init__(self, difficulty):
        self.universe = Universe(
  ``          ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.difficulty = difficulty

    def startGame(self, player):
        game = Game(player.difficulty)
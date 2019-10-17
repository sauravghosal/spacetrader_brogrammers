""" This stores all information needed for the Game -
the Player, Difficulty, Universe, and Current Region"""

from flask_wtf import FlaskForm
from wtforms import SubmitField
from Universe import Universe


class Game:
    """ The game class containing Player, Difficulty, Universe, and Current Region """
    def __init__(self):
        pass

    def start_game(self, player, difficulty):
        """Starts the game and instantiates all objects/attributes
        Keyword arguments:F
        player -- the player that's added to the game
        difficulty -- the game's difficulty
        """
        self.difficulty = difficulty
        self.player = player
        self.universe = Universe(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [])
        self.curr_region = self.universe.pick_random_region()
        


class HomePageForm(FlaskForm):
    """ The form for the landing page """
    submit = SubmitField("Start New Game!")

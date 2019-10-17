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
        player -- the player that's added to the game
        difficulty -- the game's difficulty
        """
        self.difficulty = difficulty
        self.player = player
        self.universe = Universe(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [])
        self.curr_region = self.universe.pick_random_region(
        )  # this could be moved over to player class

    def travel(self, region):
        distance = ((self.curr_region.x - region.x)**2 +
                    (self.curr_region.y - region.y)**2)**(1 / 2)
        fuel_cost = distance - self.player.pilot
        if self.player.ship.curr_fuel >= fuel_cost:
            self.player.ship.curr_fuel -= fuel_cost
            self.curr_region = region
            return True
        else:
            return False


class HomePageForm(FlaskForm):
    """ The form for the landing page """
    submit = SubmitField("Start New Game!")

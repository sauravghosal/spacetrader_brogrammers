""" This stores all information needed for the Game -
the Player, Difficulty, Universe, and Current Region"""

from flask_wtf import FlaskForm
from wtforms import SubmitField
from Universe import Universe

# Create a bandit page
# Create bandit form
# Randomize encounter chance while hitting travel
# Conditional redirection
# Fighting off the police
# Rob the trader


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
        self.curr_region = self.universe.pick_random_region()

    def travel(self, region):
        distance = (
            (self.curr_region.x_coord - region.x_coord)**2 +
            (self.curr_region.y_coord - region.y_coord)**2)**(1 / 2) / 10
        fuel_cost = distance - self.player.pilot
        if fuel_cost < 0:
            fuel_cost = 0
        if self.player.ship.current_fuel >= fuel_cost:
            self.player.ship.current_fuel -= fuel_cost
            self.curr_region = region
            return True
        else:
            return False

    def buy(self, item_key):
        base_price = self.curr_region.market.get(item_key)
        buying_price = base_price - self.player.merchant * 0.25
        if buying_price <= 0:
            buying_price = 0
        if self.player.credits >= buying_price and len(
                self.player.ship.inventory) < self.player.ship.cargo_space:
            self.player.credits -= buying_price
            self.player.ship.inventory.append(item_key)
            return True
        else:
            return False


class HomePageForm(FlaskForm):
    """ The form for the landing page """
    submit = SubmitField("Start New Game!")

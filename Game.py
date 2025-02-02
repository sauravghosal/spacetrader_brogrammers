""" This stores all information needed for the Game -
the Player, Difficulty, Universe, and Current Region"""

from flask_wtf import FlaskForm
from wtforms import SubmitField
from Universe import Universe
from NPC import NPC
from Bandit import Bandit
from Trader import Trader
from Police import Police
import random


class Game:
    """ The game class containing Player, Difficulty, Universe, and Current Region """
    def __init__(self):
        self.difficulty = None
        self.player = None
        self.universe = None
        self.curr_region = None
        self.npc = None

    def start_game(self, player, difficulty):
        """Starts the game and instantiates all objects/attributes
        player -- the player that's added to the game
        difficulty -- the game's difficulty
        """
        self.difficulty = difficulty
        self.player = player
        self.universe = Universe(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [],
            self.player.credits)
        self.curr_region = self.universe.pick_random_region()
        self.npc = None

    def travel(self, region):
        distance = (
            (self.curr_region.x_coord - region.x_coord)**2 +
            (self.curr_region.y_coord - region.y_coord)**2)**(1 / 2) / 10
        if distance != 0:
            fuel_cost = distance - self.player.pilot
            if fuel_cost < 0:
                fuel_cost = 0
            if self.player.ship.current_fuel >= fuel_cost:
                self.player.ship.current_fuel -= fuel_cost
                return True
            return False
        return False

    def buy(self, item_key, value):
        if self.player.credits >= value and len(
                self.player.ship.inventory) < self.player.ship.cargo_space:
            self.player.credits -= value
            self.player.ship.inventory.append(item_key)
            return True
        else:
            return False

    def sell(self, item_key):
        self.player.credits += self.curr_region.market.get(item_key)
        self.player.ship.inventory.remove(item_key)

    def loseCredits(self, amount):
        self.player.credits -= amount

    def loseItem(self, item_key):
        self.player.credits += 3
        self.player.ship.inventory.remove(item_key)

    def loseRandomItem(self):
        self.player.ship.inventory.remove(
            random.choice(self.player.ship.inventory))

    def refuel(self):
        fuelToFill = 100 - self.player.ship.current_fuel
        cost = fuelToFill / 3
        if cost <= self.player.credits:
            self.player.ship.current_fuel = 100
            self.player.credits -= cost
            return True
        else:
            return False

    def repair(self):
        repairs = 100 - self.player.ship.health
        cost = repairs / 3 - self.player.engineer
        if cost <= self.player.credits:
            self.player.ship.health = 100
            self.player.credits -= cost
            return True
        return False

    def loseAllCredits(self):
        self.player.credits = 0

    def loseAllItems(self):
        self.player.ship.inventory = []

    def encounter(self):
        encounterChance = random.randint(0, 1)
        if encounterChance == 1:
            if self.difficulty == "Easy":
                chance = random.randint(1, 6)
                if chance == 1:
                    randAttacker = random.randint(0, 1)
                    if randAttacker == 0:
                        if len(self.player.ship.inventory) > 0:
                            self.npc = Police()
                        else:
                            self.npc = Bandit(self.difficulty)
                    else:
                        self.npc = Bandit(self.difficulty)
                else:
                    self.npc = Trader(self.curr_region)
            if self.difficulty == "Medium":
                chance = random.randint(1, 6)
                if chance > 1 and chance < 4:
                    randAttacker = random.randint(0, 1)
                    if randAttacker == 0:
                        if len(self.player.ship.inventory) > 0:
                            self.npc = Police()
                        else:
                            self.npc = Bandit(self.difficulty)
                    else:
                        self.npc = Bandit(self.difficulty)
                else:
                    self.npc = Trader(self.curr_region)
            if self.difficulty == "Hard":
                chance = random.randint(3, 6)
                if chance > 3:
                    randAttacker = 0
                    if randAttacker == 0:
                        if len(self.player.ship.inventory) > 0:
                            self.npc = Police()
                        else:
                            self.npc = Bandit(self.difficulty)
                    else:
                        self.npc = Bandit(self.difficulty)
                else:
                    self.npc = Trader(self.curr_region)
        else:
            self.npc = None


class HomePageForm(FlaskForm):
    """ The form for the landing page """
    submit = SubmitField("Start New Game!")


class SubmitForm(FlaskForm):
    """ Submit button """
    submit = SubmitField("Continue")

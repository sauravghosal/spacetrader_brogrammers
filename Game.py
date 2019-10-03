from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Player import Player
from Universe import Universe


class Game:
    def __init__(self):
        pass

    def startGame(self, player, difficulty):
        self.difficulty = difficulty
        self.player = Player(player.pilot, player.merchant, player.fighter,
                             player.engineer, player.credits,
                             player.skill_level)
        self.universe = Universe(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [])
        self.curr_region = self.universe.pick_random_region


class homePageForm(FlaskForm):
    submit = SubmitField("Start New Game!")
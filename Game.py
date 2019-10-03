from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Player import Player


class Game:
    def __init__(self, difficulty, player):
        self.difficulty = difficulty

    def startGame(self):
        self.player = Player(player.pilot, player.merchant, player.fighter,
                             player.engineer)
        self.universe = Universe(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        universe.select_region()
        game = Game(player.difficulty)


class homePageForm(FlaskForm):
    submit = SubmitField("Start New Game!")
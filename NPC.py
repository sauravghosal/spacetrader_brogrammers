import random
from flask_wtf import FlaskForm
from wtforms import SubmitField


class NPC:
    def __init__(self):
        pass


class NPCForm(FlaskForm):
    submit = SubmitField("Select!")


class Bandit(NPC):
    # demand
    # options
    # picture
    # getImage
    def __init__(self, difficulty):
        super().__init__()
        self.demand = random.randint(1, 2)
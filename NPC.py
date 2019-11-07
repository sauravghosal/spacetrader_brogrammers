import random
from Region import Region
from flask_wtf import FlaskForm
from wtforms import SubmitField


class NPCForm(FlaskForm):
    submit = SubmitField("Select!")


difficultyValues = {"Easy": 50, "Medium": 100, "Hard": 150}


class Bandit():
    def __init__(self, difficulty):
        self.demand = random.randint(1, 5) * difficultyValues[difficulty]
        self.options = ["Flee", "Pay the Demand", "Fight!!!"]
        self.damage = difficultyValues[difficulty] % 10

    def getDemand(self):
        return self.demand

    def getOptions(self):
        return self.options

    def getDamage(self):
        return self.damage


class Trader():
    def __init__(self):
        self.options = [
            "Continue to Region", "Buy Items", "Rob Them >:)", "Negotiate"
        ]


class Police():
    def __init__(self):
        self.options = ["Forfeit the Items", "Flee", "Fight"]

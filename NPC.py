import random
from Region import Region
from flask_wtf import FlaskForm
from wtforms import SubmitField

difficultyValues = {"Easy": 50, "Medium": 100, "Hard": 150}


class NPCForm(FlaskForm):
    submit = SubmitField("Select!")


class Bandit():
    def __init__(self, difficulty):
        self.name = "Bandit"
        self.demand = random.randint(1, 5) * difficultyValues[difficulty]
        self.options = ["Flee", "Pay the Demand", "Fight!!!"]
        self.damage = difficultyValues.get(difficulty) / 10


class Trader():
    def __init__(self, region):
        self.name = "Trader"
        self.options = [
            "Continue to Region", "Buy Items", "Rob Them >:)", "Negotiate",
            "Sell items"
        ]
        self.itemKey = random.choice(list(Region.marketplace.keys()))
        self.itemValue = Region.marketplace.get(self.itemKey)


class Police():
    def __init__(self):
        self.name = "Police"
        self.options = ["Forfeit the Items", "Flee", "Fight"]

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
            "Continue to Region",
            "Buy Items",
            "Rob Them >:)",
            "Negotiate",
        ]
        self.optionsNoNegotiate = ["Buy at higher price", "Ignore", "Rob"]
        self.market = Region.marketplace.get(region.tech_level)
        self.itemKey = random.choice(list(self.market.keys()))
        self.itemValue = self.market.get(self.itemKey)


class Police():
    def __init__(self):
        self.name = "Police"
        self.options = ["Forfeit the Items", "Flee", "Fight"]

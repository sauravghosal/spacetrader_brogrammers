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
        self.damage = difficultyValues[difficulty] % 10

    def getDemand(self):
        return self.demand

    def getOptions(self):
        return self.options

    def getDamage(self):
        return self.damage

    def getName(self):
        return self.name


class Trader():
    def __init__(self):
        self.name = "Trader"
        self.options = [
            "Continue to Region", "Buy Items", "Rob Them >:)", "Negotiate",
            "Sell items"
        ]
        self.listOfItems = []
        print(Region.marketplace.keys())

    def getListOfItems(self):
        return self.listOfItems

    def getOptions(self):
        return self.options

    def getName(self):
        return self.name


class Police():
    def __init__(self):
        self.name = "Police"
        self.options = ["Forfeit the Items", "Flee", "Fight"]

    def getOptions(self):
        return self.options

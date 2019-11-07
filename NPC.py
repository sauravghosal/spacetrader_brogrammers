import random
from Region import Region
from flask_wtf import FlaskForm
from wtforms import SubmitField


class NPC:
    
    def __init__(self, difficultyValues):
        self.difficultyValues = {"Easy": "50", "Medium": "100", "Hard": "150"}




class NPCForm(FlaskForm):
    submit = SubmitField("Select!")


class Bandit(NPC):
    # demand
    # options
    # picture
    # getImage
    def __init__(self, difficulty):
        super().__init__()
        self.name = "Bandit"
        self.demand = random.randint(1,5) * int(difficultyValues[difficulty])
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



class Trader(NPC):

    def __init__(self):
        super().__init__()
        self.name = "Trader"
        self.options = ["Continue to Region", "Buy Items", "Rob Them >:)", "Negotiate"]
        self.listOfItems = []
        for key in Region.getMarketPlace.keys()
            listOfItems.append(random.choice(key))
        
    def getListOfItems(self):
        return self.listOfItems

    def getOptions(self): 
        return self.options

    def getName(self):
        return self.name
        

class Police(NPC):

    def __init__(self):
        super().__init__()
        self.options = ["Forfeit the Items", "Flee", "Fight"]
        
    def getOptions(self):
        return self.options


        

import random
from Region import Region


class NPC:
    
    def __init__(self, difficultyValues):
        self.difficultyValues = {"Easy": "50", "Medium": "100", "Hard": "150"}




class Bandit(NPC):

    def __init__(self):
        super().__init__()
        demand = random.randint(1,5) * int(difficultyValues[difficulty])
        options = ["Flee", "Pay the Demand", "Fight!!!"]
        damage = difficultyValues[difficulty] % 10

    def getDemand(self):
        return self.demand
    
    def getOptions(self):
        return self.options

    def getDamage(self):
        return self.damage

class Trader(NPC):

    def __init__(self):
        super().__init__()
        options = ["Continue to Region", "Buy Items", "Rob Them >:)", "Negotiate"]


        

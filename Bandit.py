import random
from NPC import NPC

difficultyValues = {"Easy": 50, "Medium": 100, "Hard": 150}


class Bandit(NPC):
    def __init__(self, difficulty):
        self.name = "Bandit"
        self.demand = random.randint(1, 5) * difficultyValues[difficulty]
        self.options = ["Flee", "Pay the Demand", "Fight!!!"]
        self.damage = difficultyValues.get(difficulty) / 10
        self.img = "static/bandit.jpg"

    def Interaction(self, game, option):
        result = ""
        traveled = True
        if game.player.getKarma() < 50:
            self.demand += 50 - game.player.getKarma()
        if option == 'Pay the Demand':
            if game.player.credits <= self.demand:
                if len(game.player.ship.inventory) != 0:
                    game.loseAllItems()
                    result = "You couldn't afford the demand, so you lost all your items!"
                else:
                    game.player.ship.health -= self.damage
                    result = "You couldn't afford the demand and you don't have items, so your ship took damage!"
            else:
                game.player.credits -= self.demand
                result = "You lost credits from the Bandit!"
        elif option == 'Flee':
            if (game.player.pilot <= random.randint(0, 16)):
                game.loseAllCredits()
                game.player.ship.health -= self.damage
                result = "You are unable to flee, lost all your credits, and took ship damage!"
            else:
                result = "You successfully fled back to the previous region!"
                traveled = False
        else:
            game.player.loseKarma(10)
            if game.player.fighter >= random.randint(0, 16):
                game.player.credits += 100
                result = "You stole credits from the Bandit!"
            else:
                game.loseAllCredits()
                game.player.ship.health -= 10
                result = "You lost all your credits & took ship damage!"
        return [result, traveled]

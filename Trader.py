from NPC import NPC
import random
from Region import Region
import math
from TechLevel import TechLevel

class Trader(NPC):
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
        while self.itemKey == 'universe':
            self.itemKey = random.choice(list(self.market.keys()))
        self.itemValue = self.market.get(self.itemKey)
        self.img = "static/trader.jpg"

    def Interaction(self, game, option):
        traveled = True
        result = ""
        if game.player.getKarma() > 50:
            self.itemValue -= math.floor(game.player.getKarma() / 10)
        else:
            self.itemValue = self.itemValue
        if option == 'Buy Items':
            if game.player.credits >= self.itemValue:
                game.buy(self.itemKey, self.itemValue)
                game.player.addKarma(5)

                result = "You bought the trader's item!"

            else:
                result = "You don't have enough money to buy the item!"
        elif option == 'Continue to Region':
            result = "You ignored the trader! Press button to continue to next region!"
        elif option == 'Rob Them >:)':
            if game.player.fighter >= random.randint(0, 16):
                game.player.ship.inventory.append(self.itemKey)
                result = "You robbed the trader! Press button to continue to next region"
                game.player.loseKarma(10)
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
                game.player.loseKarma(10)

        elif option == 'Negotiate':
            if game.player.merchant >= random.randint(0, 16):
                game.buy(self.itemKey, self.itemValue)
                game.player.credits += self.itemValue / 2
                result = "You successfully negotiated and bought the item at a reduced price!"
            else:
                result = "Not able to Negotiate"
        return [result, traveled]

    def Negotiate(self, game, negotiateOption):
        self.itemKey = self.itemKey
        offeredCost = self.itemValue
        result = ''
        if negotiateOption == 'Buy at higher price':
            game.buy(offeredItem, offeredCost)
            game.player.credits -= 2 * offeredCost
            result = "You bought the item at an increased price!"
        elif negotiateOption == 'Ignore':
            result = "You ignored the trader! Press button to continue to next region!"
        elif negotiateOption == "Rob":
            if game.player.fighter >= random.randint(0, 16):
                game.player.ship.inventory.append(self.itemKey)
                result = "You successfully robbed the trader!"
                game.player.loseKarma(10)
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
                game.player.loseKarma(10)
        return result

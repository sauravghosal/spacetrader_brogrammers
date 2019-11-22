from NPC import NPC
import random
from Region import Region
import math
from TechLevel import TechLevel

class Trader(NPC):
    def __init__(self):
        self.name = "Trader"
        self.options = [
            "Continue to Region",
            "Buy Items",
            "Rob Them >:)",
            "Negotiate",
        ]
        self.optionsNoNegotiate = ["Buy at higher price", "Ignore", "Rob"]
        self.market = Region.marketplace.get(TechLevel(random.randint(0, 6)))
        self.itemKey = random.choice(list(self.market.keys()))
        self.itemValue = self.market.get(self.itemKey)
        self.img = "static/trader.jpg"

    def Interaction(self, game, option):
        traveled = True
        result = ""
        offeredItem = self.itemKey
        if game.player.getKarma() > 50:
            offeredCost = self.itemValue - math.floor(game.player.getKarma / 10)
        else:
            offeredCost = self.itemValue
        if option == 'Buy Items':
            if game.player.credits >= offeredCost:
                game.buy(offeredItem)
                game.player.addKarma(5)
                result = "You bought the trader's item!"

            else:
                result = "You don't have enough money to buy the item!"
        elif option == 'Continue to Region':
            result = "You ignored the trader! Press button to continue to next region!"
        elif option == 'Rob Them >:)':
            if game.player.fighter >= random.randint(0, 16):
                game.player.ship.inventory.append(offeredItem)
                result = "You robbed the trader! Press button to continue to next region"
                game.player.loseKarma(10)
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
                game.player.loseKarma(10)

        elif option == 'Negotiate':
            if game.player.merchant >= random.randint(0, 16):
                game.buy(offeredItem)
                game.player.credits += offeredCost / 2
                result = "You successfully negotiated and bought the item at a reduced price!"
            else:
                result = "Not able to Negotiate"
        return [result, traveled]

    def Negotiate(self, game, negotiateOption):
        offeredItem = self.itemKey
        offeredCost = self.itemValue
        result = ''
        if negotiateOption == 'Buy at higher price':
            game.buy(offeredItem)
            game.player.credits -= 2 * offeredCost
            result = "You bought the item at an increased price!"
        elif negotiateOption == 'Ignore':
            result = "You ignored the trader! Press button to continue to next region!"
        elif negotiateOption == "Rob":
            if game.player.fighter >= random.randint(0, 16):
                game.player.ship.inventory.append(offeredItem)
                result = "You successfully robbed the trader!"
                game.player.loseKarma(10)
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
                game.player.loseKarma(10)
        return result

import random
from flask_wtf import FlaskForm
from wtforms import SubmitField
from Region import Region

difficultyValues = {"Easy": 50, "Medium": 100, "Hard": 150}


class NPCForm(FlaskForm):
    submit = SubmitField("Select!")


class Bandit():
    def __init__(self, difficulty):
        self.name = "Bandit"
        self.demand = random.randint(1, 5) * difficultyValues[difficulty]
        self.options = ["Flee", "Pay the Demand", "Fight!!!"]
        self.damage = difficultyValues.get(difficulty) / 10
        self.img = "static/newbandit.jpg"

    def BanditInteraction(self, game, option):
        result = ""
        traveled = True
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
            if game.player.fighter >= random.randint(0, 16):
                game.player.credits += 100
                result = "You stole credits from the Bandit!"
            else:
                game.loseAllCredits()
                game.player.ship.health -= self.damage
                result = "You lost all your credits & took ship damage!"
        return [result, traveled]


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
        self.img = "static/trader.jpg"

    def TraderInteraction(self, game, option):
        traveled = True
        result = ""
        offeredItem = self.itemKey
        offeredCost = self.itemValue
        if option == 'Buy Items':
            if game.player.credits >= offeredCost:
                game.buy(offeredItem)
                result = "You bought the trader's item!"
            else:
                result = "You don't have enough money to buy the item!"
        elif option == 'Continue to Region':
            result = "You ignored the trader! Press button to continue to next region!"
        elif option == 'Rob Them >:)':
            if game.player.fighter >= random.randint(0, 16):
                game.player.ship.inventory.append(offeredItem)
                result = "You robbed the trader! Press button to continue to next region"
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
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
            else:
                game.player.ship.health -= 10
                result = "You failed to rob the trader, so your ship took damage!"
        return result


class Police():
    def __init__(self):
        self.name = "Police"
        self.options = ["Forfeit the Items", "Flee", "Fight"]
        self.img = "static/police.jpg"

    def PoliceInteraction(self, game, option):
        traveled = True
        result = ""
        if option == 'Forfeit the Items':
            game.loseAllItems()
            result = "You lost all your items!"
        elif option == 'Flee':
            if game.player.pilot <= random.randint(0, 16):
                game.loseRandomItem()
                game.player.ship.health -= 10
                game.loseMoney(10)
                traveled = False
                result = "You lost the item, damaged ship health, and lost credits!"
            else:
                traveled = False
                game.player.ship.current_fuel -= 10  # fix
        elif option == 'Fight':
            if game.player.fighter <= random.randint(0, 16):
                result = "You successfully fought off the police!"
            else:
                game.loseAllItems()
                game.player.ship.health -= 10
                game.loseMoney(10)
                traveled = False
                result = "You lost all your items, your ship took damage, and you lost credits!"
        return [result, traveled]

import random


def TraderInteraction(game, option):
    traveled = True
    result = ""
    offeredItem = game.npc.itemKey
    offeredCost = game.npc.itemValue
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


def Negotiate(game, negotiateOption):
    offeredItem = game.npc.itemKey
    offeredCost = game.npc.itemValue
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

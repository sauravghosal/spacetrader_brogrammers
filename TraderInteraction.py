import random


def TraderInteraction(game, option):
    traveled = True
    result = ""
    offeredItem = game.npc.itemKey
    offeredCost = game.npc.itemValue
    if option == 'Buy Items':
        game.buy(offeredItem)
        result = "You bought the trader's item!"
    elif option == 'Rob Them >:)':
        if game.player.fighter >= random.randint(0, 16):
            game.player.ship.inventory.append(offeredItem)
            result = "You robbed the trader!"
        else:
            game.player.ship.health -= 10
            result = "Your ship took damage!"
    elif option == 'Negotiate':
        if game.player.merchant >= random.randint(0, 16):
            game.buy(offeredItem)
            game.player.credits += offeredCost / 2
            result = "You bought the item at a reduced price!"
        else:
            result = "Not able to Negotiate"
    return [result, traveled]


def Negotiate(game, negotiateOption):
    offeredItem = game.npc.itemKey
    offeredCost = game.npc.itemValue
    if negotiateOption == 'Buy':
        game.buy(offeredItem)
        game.player.credits -= 2 * offeredCost
        result = "You bought the item at an increased price!"
    # elif negotiateOption == 'Ignore':
    elif negotiateOption == "Rob":
        if game.player.fighter >= random.randint(0, 16):
            game.player.ship.inventory.append(offeredItem)
            result = "You successfully robbed the trader!"
        else:
            game.player.ship.health -= 10
            result = "Your ship took damage!"
    return [result, True]

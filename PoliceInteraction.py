import random


def PoliceInteraction(game, option, region):
    result = ""
    traveled = True
    if option == 'Forfeit the Items':
        game.loseAllItems()
        result = "Lost all your items"
    elif option == 'Flee':
        if (game.player.pilot <= random.randint(0, 16)):
            game.loseRandomItem()
            game.player.ship.health -= 10
            game.loseMoney(10)
            game.curr_region = region
    elif option == 'Fight':
        if (game.player.fighter <= random.randint(0, 16)):
            game.curr_region = region
        else:
            game.loseAllItems()
            game.player.ship.health -= 10
            game.loseMoney(10)
            game.curr_region = region
    return result
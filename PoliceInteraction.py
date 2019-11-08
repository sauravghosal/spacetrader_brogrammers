import random

def PoliceInteraction(game, option):
    traveled = True
    result = ""
    if option == 'Forfeit the Items':
        game.loseAllItems()
        result = "You lost all your items!"
    elif option == 'Flee':
        if (game.player.pilot <= random.randint(0, 16)):
            game.loseRandomItem()
            game.player.ship.health -= 10
            game.loseMoney(10)
            traveled = False
            result = "You lost the item, damaged ship health, and lost credits!"
    elif option == 'Fight':
        if (game.player.fighter <= random.randint(0, 16)):
            result = "You successfully fought off the police!"
        else:
            game.loseAllItems()
            game.player.ship.health -= 10
            game.loseMoney(10)
            traveled = False
            result = "You lost all your items, your ship took damage, and you lost credits!"
    return [result, traveled]

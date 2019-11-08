import random


# when fleeing go back to travel page
def BanditInteraction(game, option):
    result = ""
    traveled = True
    if option == 'Pay the Demand':
        if game.player.credits <= game.npc.demand:
            if len(game.player.ship.inventory) != 0:
                game.loseAllItems()
                result = "You couldn't afford the demand, so you lost all your items!"
            else:
                game.player.ship.health -= game.npc.damage
                result = "You couldn't afford the demand and you don't have items, so your ship took damage!"
        else:
            game.player.credit -= game.npc.demand
            result = "You lost credits from the Bandit!"
    elif option == 'Flee':
        if (game.player.pilot <= random.randint(0, 16)):
            game.loseAllCredits()
            game.player.ship.health -= game.npc.damage
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
            game.player.ship.health -= game.npc.damage
            result = "You lost all your credits & took ship damage!"
    return [result, traveled]

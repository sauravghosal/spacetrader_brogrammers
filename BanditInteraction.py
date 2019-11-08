import random


# when fleeing go back to travel page
def BanditInteraction(game, option):
    result = ""
    if option == 'Pay the Demand':
        if game.player.credits <= game.npc.demand:
            if len(game.player.ship.inventory):
                game.loseAllItems()
                result = "Lost all your items"
            else:
                game.player.ship.health -= game.npc.damage
                result = "You took ship damage"
        else:
            game.player.credit -= game.npc.demand
            result = "You lost credits!"
    elif option == 'Flee':
        if (game.player.pilot >= random.randint(0, 16)):
            game.loseAllMoney()
            game.player.ship.health -= game.npc.damage
            result = "You lost all your credits & took ship damage!"
    else:
        if game.player.fighter >= random.randint(0, 16):
            game.player.credits += 100
            result = "You stole credits from bandit"
        else:
            game.loseAllCredits()
            game.player.ship.health -= game.npc.damage
            result = "You lost all your credits & took ship damage!"
    return result

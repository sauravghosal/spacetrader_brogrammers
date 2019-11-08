import random


# when fleeing go back to travel page
def BanditInteraction(game, option):
    result = ""
    traveled = True
    if option == 'Pay the Demand':
        if game.player.credits <= game.npc.demand:
            if len(game.player.ship.inventory):
                game.loseAllItems()
                result = "You lost all your items"
            else:
                game.player.ship.health -= game.npc.damage
                result = "You don't have enough credits to pay the demand, and your ship takes damage!"
        else:
            game.player.credit -= game.npc.demand
            result = "You lost credits!"
    elif option == 'Flee':
        if (game.player.pilot <= random.randint(0, 16)):
            game.loseAllCredits()
            game.player.ship.health -= game.npc.damage
            result = "You lost all your credits & took ship damage!"
        else:
            result = "You successfully flee."
            traveled = False
    else:
        if game.player.fighter >= random.randint(0, 16):
            game.player.credits += 100
            result = "You stole credits from bandit"
        else:
            game.loseAllCredits()
            game.player.ship.health -= game.npc.damage
            result = "You lost all your credits & took ship damage!"
<<<<<<< HEAD
    return [result, traveled]
=======
    return [result, traveled]
>>>>>>> aa3ace4efb43de29c5c41d0b5f9ae83164199ff1

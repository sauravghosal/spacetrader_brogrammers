from NPC import NPC
import random


class Police(NPC):
    def __init__(self):
        self.name = "Police"
        self.options = ["Forfeit the Items", "Flee", "Fight"]
        self.img = "static/police.jpg"

    def Interaction(self, game, option):
        traveled = True
        result = ""
        if option == 'Forfeit the Items':
            game.loseAllItems()
            result = "You lost all your items!"
        elif option == 'Flee':
            if game.player.pilot <= random.randint(0, 16):
                game.loseRandomItem()
                game.player.ship.health -= 100
                game.loseMoney(10)
                traveled = False
                result = "You lost the item, damaged ship health, and lost credits!"
            else:
                traveled = False
                game.player.ship.current_fuel -= 100  # fix
        elif option == 'Fight':
            if game.player.fighter >= random.randint(0, 16):
                result = "You successfully fought off the police!"
            else:
                game.loseCredits()
                game.player.ship.health -= 100
                game.loseMoney(10)
                traveled = False
                result = "You lost all your items, your ship took damage, and you lost credits!"
        return [result, traveled]

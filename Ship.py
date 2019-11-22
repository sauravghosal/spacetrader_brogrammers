import random


class Ship:
    names = [
        "Starship", "Galactica", "Starfleet", "Battle Star", "Andromeda",
        "Nebula", "Titan"
    ]

    def __init__(self):
        self.type = random.randint(0, len(self.names))
        self.cargo_space = 5
        self.FUEL_CAPACITY = 100
        self.current_fuel = self.FUEL_CAPACITY
        self.health = 100
        self.inventory = []

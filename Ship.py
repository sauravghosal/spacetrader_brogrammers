import random


class ship:
    names = [
        "Starship", "Galactica", "Starfleet", "Battle Star", "Andromeda",
        "Nebula", "Titan"
    ]

    def __init__(self):
        self.type = random.randint(0, len(self.names))
        self.cargo_space = 5
        self.fuel_capacity = 100
        self.current_fuel = self.fuel_capacity
        self.health = 100
        self.inventory = []

import random


class Ship:
    names = [
        "Starship", "Galactica", "Starfleet", "Battle Star", "Andromeda",
        "Nebula", "Titan"
    ]

    def __init__(self):
        self.type = random.randint(0, len(self.names))
        self.cargo_space = 20
        self.fuel_capacity = 100
        self.health = 100

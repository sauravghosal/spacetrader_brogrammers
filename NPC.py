import random


class NPC:
    def __init__(self):
        pass


class Bandit(NPC):
    # demand
    #
    def __init__(self, difficulty):
        super().__init__()
        self.demand = random.randint(1, 2)
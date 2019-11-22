from enum import Enum


class TechLevel(Enum):
    PRE_AGRICULTURE = 0
    AGRICULTURE = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    INDUSTRIAL = 4
    MODERN = 5
    FUTURISTIC = 6

    def __str__(self):
        return str(self.name)

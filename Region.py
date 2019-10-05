class Region:
    def __init__(self, x, y, techLevel, name, number):
        self.x = x
        self.y = y
        self.techLevel = techLevel
        self.name = name
        self.number = number

    def __str__(self):
        return f'Name: {self.name}, Location: ({self.x}, {self.y}), TechLevel: {self.techLevel}'

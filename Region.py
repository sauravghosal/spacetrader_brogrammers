class Region:
    def __init__(self, x_coord, y_coord, tech_level, name, number):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.tech_level = tech_level
        self.name = name
        self.number = number
        self.fuel_cost = fuel_cost

    def __str__(self):
        return f'Name: {self.name}, Location: ({self.x_coord}, {self.y_coord}), tech_level: {self.tech_level}'

from TechLevel import TechLevel


class Region:
    marketplace = {TechLevel(0): {'rock': 1, 'skin': 2, 'fur': 3, 'bone': 4, 'spear': 5, 'bat': 6, 'stick': 7, 'pebble': 8, 'meat': 9, 'stone': 10},
                   TechLevel(1): {'berry': 1, 'wheat': 2, 'grain': 3, 'shovel': 4, 'corn': 5, 'goat': 6, 'rice': 7, 'chicken': 8, 'cow': 9, 'hoe': 10},
                   TechLevel(2): {'mutton': 1, 'sword': 2, 'horse': 3, 'javelin': 4, 'helmet': 5, 'chainmail': 6, 'bronze': 7, 'silver': 8, 'gold': 9, 'armor': 10},
                   TechLevel(3): {'paint': 1, 'canvas': 2, 'tapestry': 3, 'Jesus': 4, 'The Bible': 5, 'gowns': 6, 'corsets': 7, 'lute': 8, 'statue': 9, 'painting': 10},
                   TechLevel(4): {'steel': 1, 'gear': 2, 'iron': 3, 'factory': 4, 'Moses': 5, 'hammer': 6, 'wheel': 7, 'steam engine': 8, 'child': 9, 'sewing machine': 10},
                   TechLevel(5): {'computer': 1, 'phone': 2, 'bacon': 3, 'airpods': 4, 'jacket': 5, 'ninja star': 6, 'table': 7, 'synthesizer': 8, 'shoe': 9, 'memes': 10},
                   TechLevel(6): {'magic beans': 1, 'deathstar': 2, 'theremin': 3, 'hovercraft': 4, 'invisibility cloak': 5, 'teleporter': 6, 'time machine': 7, 'power': 8, 'ho': 9, 'robot': 10},
                  }  
    
    def __init__(self, x_coord, y_coord, tech_level, name, number):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.tech_level = tech_level
        self.name = name
        self.number = number
        self.market = self.marketplace.get(tech_level)

    def __str__(self):
        return f'Name: {self.name}, Location: ({self.x_coord}, {self.y_coord}), tech_level: {self.tech_level}'

    def getMarketPlace(self):
        return self.marketplace
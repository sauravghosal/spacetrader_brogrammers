from TechLevel import TechLevel


class Region:
    marketplace = {TechLevel(0): {'rock': 10, 'skin': 20, 'fur': 30, 'bone': 40, 'spear': 50, 'bat': 60, 'stick': 70, 'pebble': 80, 'meat': 90, 'stone': 100},
                   TechLevel(1): {'berry': 10, 'wheat': 20, 'grain': 30, 'shovel': 40, 'corn': 50, 'goat': 60, 'rice': 70, 'chicken': 80, 'cow': 90, 'hoe': 100},
                   TechLevel(2): {'mutton': 10, 'sword': 20, 'horse': 30, 'javelin': 40, 'helmet': 50, 'chainmail': 60, 'bronze': 70, 'silver': 80, 'gold': 90, 'armor': 100},
                   TechLevel(3): {'paint': 10, 'canvas': 20, 'tapestry': 30, 'Jesus': 40, 'The Bible': 50, 'gowns': 60, 'corsets': 70, 'lute': 80, 'statue': 90, 'painting': 100},
                   TechLevel(4): {'steel': 10, 'gear': 20, 'iron': 30, 'factory': 40, 'Moses': 50, 'hammer': 60, 'wheel': 70, 'steam engine': 80, 'child': 90, 'sewing machine': 100},
                   TechLevel(5): {'computer': 10, 'phone': 20, 'bacon': 30, 'airpods': 40, 'jacket': 50, 'ninja star': 60, 'table': 70, 'synthesizer': 80, 'shoe': 90, 'memes': 100},
                   TechLevel(6): {'magic beans': 10, 'deathstar': 20, 'theremin': 30, 'hovercraft': 40, 'invisibility cloak': 50, 'teleporter': 60, 'time machine': 70, 'power': 80, 'ho': 90, 'robot': 100},
                  }  
    
    def __init__(self, x_coord, y_coord, tech_level, name, number):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.tech_level = tech_level
        self.name = name
        self.number = number
        self.market = self.marketplace.get(tech_level)

    def __str__(self):
        return f'Name: {self.name}, Location: ({self.x_coord}), {self.tech_level}'

    def getMarketPlace(self):
        return self.marketplace
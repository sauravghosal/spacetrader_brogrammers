import random
from flask_wtf import FlaskForm
from wtforms import SubmitField
from Region import Region
import TechLevel


class Universe():  #params list of Regions
    #Universe is a list of regions

    def __init__(self, region_names, regions):
        self.region_names = region_names
        coords_list = []
        self.regions = regions
        marketplace = { TechLevel.TechLevel(0): { 'rock': 1, 'skin': 2, 'fur': 3, 'bone': 4, 'spear': 5, 'bat': 6, 'stick': 7, 'pebble': 8, 'meat': 9, 'stone': 10},
                        TechLevel.TechLevel(0): { 'berry': 1, 'wheat': 2, 'grain': 3, 'shovel': 4, 'corn': 5, 'goat': 6, 'rice': 7, 'chicken': 8, 'cow': 9, 'hoe': 10},
                        TechLevel.TechLevel(0): { 'mutton': 1, 'sword': 2, 'horse': 3, 'javelin': 4, 'helmet': 5, 'chainmail': 6, 'bronze': 7, 'silver': 8, 'gold': 9, 'armor': 10},
                        TechLevel.TechLevel(0): { 'paint': 1, 'canvas': 2, 'tapestry': 3, 'Jesus': 4, 'The Bible': 5, 'gowns': 6, 'corsets': 7, 'lute': 8, 'statue': 9, 'painting': 10},
                        TechLevel.TechLevel(0): { 'steel': 1, 'gear': 2, 'iron': 3, 'factory': 4, 'Moses': 5, 'hammer': 6, 'wheel': 7, 'steam engine': 8, 'child': 9, 'sewing machine': 10},
                        TechLevel.TechLevel(0): { 'computer': 1, 'phone': 2, 'bacon': 3, 'airpods': 4, 'jacket': 5, 'ninja star': 6, 'table': 7, 'synthesizer': 8, 'shoe': 9, 'memes': 10},
                        TechLevel.TechLevel(0): { 'magic beans': 1, 'deathstar': 2, 'theremin': 3, 'hovercraft': 4, 'invisibility cloak': 5, 'teleporter': 6, 'time machine': 7, 'power': 8, 'ho': 9, 'robot': 10},
                        
        for i in range(0, len(region_names)):
            coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            while coords in coords_list:
                coords = (5 * random.randint(-40, 40),
                          5 * random.randint(-40, 40))
            coords_list.append(coords)
            tech_level = TechLevel.TechLevel(random.randint(0, 6))
            regions.append(
                Region(coords[0], coords[1], tech_level, region_names[i], i))

    def pick_random_region(self):
        return self.regions[random.randint(0, 9)]

    def find_region(self, index):
        return self.regions[index]

    # Prints all regions inside universe
    def __str__(self):
        ans = ""
        for i in range(0, len(self.regions)):
            ans += "Region " + str(i) + " " + str(self.regions[i])
        return ans


# Add functionality here
class UniverseForm(FlaskForm):
    submit = SubmitField("Let's travel!")

import random
from flask_wtf import FlaskForm
from wtforms import SubmitField
from Region import Region
import TechLevel


class Universe():  #params list of Regions
    #Universe is a list of regions

    def __init__(self, region_names, regions, price):
        self.region_names = region_names
        coords_list = []
        self.regions = regions
        for i in range(0, len(region_names)):
            coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            while coords in coords_list:
                coords = (5 * random.randint(-40, 40),
                          5 * random.randint(-40, 40))
            coords_list.append(coords)
            tech_level = TechLevel.TechLevel(random.randint(0, 6))
            regions.append(
                Region(coords[0], coords[1], tech_level, region_names[i], i))
        self.pick_random_region().market['universe'] = price * 1.25

    def pick_random_region(self):
        return self.regions[random.randint(0, 9)]

    def find_region(self, index):
        return self.regions[index]

    def __str__(self):
        ans = ""
        for i in range(0, len(self.regions)):
            ans += "Region " + str(i) + " " + str(self.regions[i])
        return ans


# Add functionality here
class UniverseForm(FlaskForm):
    submit = SubmitField("Let's travel!")

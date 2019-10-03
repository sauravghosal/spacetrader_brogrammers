import TechLevel
import random
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Region import Region


class Universe():  #params list of Regions
    #Universe is a list of regions

    def __init__(self, regionNames):
        self.regionNames = regionNames
        self.regions = []
        self.coordsList = []
        for i in regionNames:
            coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            while coords in coordsList:
                coords = (5 * random.randint(-40, 40),
                          5 * random.randint(-40, 40))
            coordsList.append(coords)
            techLevel = random.choice(list(TechLevel))
            regions.append(
                Region(coords[0], coords[1], techLevel, regionNames[i]))

    def select_region(self):
        return self.regions[random.randint(0,9)]


class UniverseForm():
    next_region = SubmitField("Next Region")

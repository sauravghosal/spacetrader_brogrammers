import TechLevel
from Region import Region
import random

class Universe(): #params list of Regions
    #Universe is a list of regions

    def __init__ (self, regionNames,regions):
        self.regionNames = regionNames
        coordsList = []
        self.regions = regions
        for i in regionNames:
            coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            while coords in coordsList:
                coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            coordsList.append(coords)
            techLevel = TechLevel.TechLevel(random.randint(0,6))
            regions.append(Region(coords[0], coords[1], techLevel, i)) 

    
        
        

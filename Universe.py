import TechLevel
class Universe(): #params list of Regions
    #Universe is a list of regions
    def __init__ (regionNames):
        self.regionNames = regionNames
        self.regions = []
        self.coordsList = []
        for i in regionNames:
            coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            while coords in coordsList:
                coords = (5 * random.randint(-40, 40), 5 * random.randint(-40, 40))
            techLevel = random.choice(list(TechLevel))
            regions.append(Region(coords[0], coords[1], techLevel, regionNames[i])) 

        
        

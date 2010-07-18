#Variations of item: Large Cargohold Optimization I (2 of 2) [Module]
#Variations of item: Medium Cargohold Optimization I (2 of 2) [Module]
#Variations of item: Small Cargohold Optimization I (2 of 2) [Module]
from customEffects import boost
def skillFreightBonus(self, fitting, state):
    boost(fitting.ship, "capacity", "cargoCapacityBonus", self.item)
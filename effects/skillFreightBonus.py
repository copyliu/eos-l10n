#Used by: Item: Cargohold Optimization
from customEffects import boost
def skillFreightBonus(self, fitting, state):
    boost(fitting.ship, "capacity", "cargoCapacityBonus", self.item)
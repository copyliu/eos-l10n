#Used by: Ship: Worm
from customEffects import increase
def shipBonusDroneCapacityGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    increase(fitting.ship, "droneCapacity", "shipBonusGF", self.item, extraMult = level)
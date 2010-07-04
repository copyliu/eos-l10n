#Used by: Ship: Exequror
from customEffects import boost
def shipCargoCapacityGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boost(fitting.ship, "capacity", "shipBonusGC2", self.item, extraMult = level)
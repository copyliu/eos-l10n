#Used by: Ship: Bantam
from customEffects import boost
def shipCargoBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "capacity", "shipBonusCF", self.item, extraMult = level)
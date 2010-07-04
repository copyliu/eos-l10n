#Used by: Ship: Chimera
#               Wyvern
from customEffects import increase
def carrierCaldariDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierCaldariBonus1",
             self.item, extraMult = level)
#Used by: Ship: Archon
#               Aeon
from customEffects import increase
def carrierAmarrDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierAmarrBonus1",
             self.item, extraMult = level)
#Used by: Ship: Nidhoggur
#               Hel
from customEffects import increase
def carrierMinmatarDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierMinmatarBonus1",
             self.item, extraMult = level)
#Used by: Ship: Thanatos
#               Nyx
from customEffects import increase
def carrierGallenteDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierGallenteBonus1",
             self.item, extraMult = level)
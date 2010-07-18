#Items from market group: Ships > Carriers > Gallente (2 of 2)
from customEffects import increase
def carrierGallenteDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierGallenteBonus1",
             self.item, extraMult = level)
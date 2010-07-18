#Items from market group: Ships > Carriers > Amarr (2 of 2)
from customEffects import increase
def carrierAmarrDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierAmarrBonus1",
             self.item, extraMult = level)
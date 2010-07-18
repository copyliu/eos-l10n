#Items from market group: Ships > Carriers > Minmatar (2 of 2)
from customEffects import increase
def carrierMinmatarDroneMax1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Carrier")
    increase(fitting.ship, "_maxActiveDrones", "carrierMinmatarBonus1",
             self.item, extraMult = level)
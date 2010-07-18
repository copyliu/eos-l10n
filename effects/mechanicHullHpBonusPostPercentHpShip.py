#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Armor Implants (3 of 3)
#Item: Mechanic
from customEffects import boost
def mechanicHullHpBonusPostPercentHpShip(self, fitting, level = 1):
    boost(fitting.ship, "hp", "hullHpBonus", self.item, extraMult = level)
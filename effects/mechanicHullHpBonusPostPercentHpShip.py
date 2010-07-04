#Used by: Skill: Mechanic
from customEffects import boost
def mechanicHullHpBonusPostPercentHpShip(self, fitting, level = 1):
    boost(fitting.ship, "hp", "hullHpBonus", self.item, extraMult = level)
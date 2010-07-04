#Used by: Skill: Navigation
#         Item : Auxiliary Thrusters
#                Snake Implant Set
from customEffects import boost
def navigationVelocityBonusPostPercentMaxVelocityShip(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
    boost(fitting.ship, "maxVelocity", "velocityBonus", self.item,
          useStackingPenalty = penalized, extraMult = level)

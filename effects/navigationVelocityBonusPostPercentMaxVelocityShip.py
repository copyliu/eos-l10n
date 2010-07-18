#Items from group: Cyberimplant (11 of 138) [Implant]
#Variations of item: Large Auxiliary Thrusters I (2 of 2) [Module]
#Variations of item: Medium Auxiliary Thrusters I (2 of 2) [Module]
#Variations of item: Small Auxiliary Thrusters I (2 of 2) [Module]
#Item: Navigation [Skill]
from customEffects import boost
def navigationVelocityBonusPostPercentMaxVelocityShip(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
    boost(fitting.ship, "maxVelocity", "velocityBonus", self.item,
          useStackingPenalty = penalized, extraMult = level)

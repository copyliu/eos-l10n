#Items from category: Implant (8 of 471)
#Variations of item: Large Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Medium Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Small Low Friction Nozzle Joints I (2 of 2) [Module]
#Item: Evasive Maneuvering [Skill]
#Item: Spaceship Command [Skill]
from customEffects import boost
def evasiveManeuveringAgilityBonusPostPercentAgilityShip(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
        
    boost(fitting.ship, "agility", "agilityBonus", self.item,
          useStackingPenalty = penalized, extraMult = level)

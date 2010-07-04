#Used by: Skill: Evasive Maneuvering
#                Spaceship Command
#          Item: Low Friction Nozzle Joints
#                Nomad Implant Set
#                Rogue CY-series hardwirings
from customEffects import boost
def evasiveManeuveringAgilityBonusPostPercentAgilityShip(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
        
    boost(fitting.ship, "agility", "agilityBonus", self.item,
          useStackingPenalty = penalized, extraMult = level)

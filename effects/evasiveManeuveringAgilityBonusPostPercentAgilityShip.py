#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Navigation Implants (3 of 4)
#Variations of item: Large Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Medium Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Small Low Friction Nozzle Joints I (2 of 2) [Module]
#Item: Evasive Maneuvering [Skill]
#Item: Low-grade Nomad Alpha [Implant]
#Item: Low-grade Nomad Beta [Implant]
#Item: Low-grade Nomad Delta [Implant]
#Item: Low-grade Nomad Epsilon [Implant]
#Item: Low-grade Nomad Gamma [Implant]
#Item: Spaceship Command [Skill]
from customEffects import boost
def evasiveManeuveringAgilityBonusPostPercentAgilityShip(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
        
    boost(fitting.ship, "agility", "agilityBonus", self.item,
          useStackingPenalty = penalized, extraMult = level)

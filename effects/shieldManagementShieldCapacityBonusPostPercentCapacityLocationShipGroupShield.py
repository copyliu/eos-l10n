#Items from group: Cyber Shields (4 of 13) [Implant]
#Items from group: Rig Shield (6 of 54) [Module]
#Item: Shield Management [Skill]
from customEffects import boost
def shieldManagementShieldCapacityBonusPostPercentCapacityLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldCapacity", "shieldCapacityBonus",
          self.item, extraMult = level)
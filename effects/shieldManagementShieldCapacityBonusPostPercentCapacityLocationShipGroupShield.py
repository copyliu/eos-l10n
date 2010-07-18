#Items from group: Cyber Shields (4 of 13)
#Items from group: Rig Shield (6 of 54)
#Item: Shield Management
from customEffects import boost
def shieldManagementShieldCapacityBonusPostPercentCapacityLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldCapacity", "shieldCapacityBonus",
          self.item, extraMult = level)
#Used by: Item : Core Defence Field Extender
#         Skill: Shield Management
from customEffects import boost
def shieldManagementShieldCapacityBonusPostPercentCapacityLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldCapacity", "shieldCapacityBonus",
          self.item, extraMult = level)
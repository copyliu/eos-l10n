#Used by: Skill: Engineering
#           Rig: Ancillary Current Router
from customEffects import boost
def engineeringPowerEngineeringOutputBonusPostPercentPowerOutputLocationShipGroupPowerCore(self, fitting, state = None, level = 1):
    boost(fitting.ship, "powerOutput", "powerEngineeringOutputBonus",
          self.item, extraMult = level)
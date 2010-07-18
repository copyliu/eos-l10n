#Items from group: Cyber Shields (4 of 13) [Implant]
#Items from group: Rig Shield (6 of 54) [Module]
#Item: Shield Operation [Skill]
from customEffects import boost
def shieldOperationRechargeratebonusPostPercentRechargeRateLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldRechargeRate", "rechargeratebonus",
          self.item, extraMult = level)
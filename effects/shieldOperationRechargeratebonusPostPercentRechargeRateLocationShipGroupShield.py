#Used by: Skill: Shield Operation
#         Item : Core Defence Field Purger
from customEffects import boost
def shieldOperationRechargeratebonusPostPercentRechargeRateLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldRechargeRate", "rechargeratebonus",
          self.item, extraMult = level)
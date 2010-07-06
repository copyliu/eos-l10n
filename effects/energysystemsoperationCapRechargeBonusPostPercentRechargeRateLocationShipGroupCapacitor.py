#Used by: Skill: Energy Systems Operation
#           Rig: Capacitor Control Circuit
from customEffects import boost
def energysystemsoperationCapRechargeBonusPostPercentRechargeRateLocationShipGroupCapacitor(self, fitting, state = None, level = 1):
    boost(fitting.ship, "rechargeRate", "capRechargeBonus",
          self.item, extraMult = level)
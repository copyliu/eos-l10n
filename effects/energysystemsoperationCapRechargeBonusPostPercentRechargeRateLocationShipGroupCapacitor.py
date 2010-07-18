#Items from group: Cyber Engineering (3 of 21) [Implant]
#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Systems Operation [Skill]
from customEffects import boost
def energysystemsoperationCapRechargeBonusPostPercentRechargeRateLocationShipGroupCapacitor(self, fitting, state = None, level = 1):
    boost(fitting.ship, "rechargeRate", "capRechargeBonus",
          self.item, extraMult = level)
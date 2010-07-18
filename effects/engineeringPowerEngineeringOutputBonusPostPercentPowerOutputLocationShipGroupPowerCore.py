#Items from group: Cyber Engineering (3 of 21)
#Items from group: Rig Energy Grid (6 of 30)
#Item: Engineering
from customEffects import boost
def engineeringPowerEngineeringOutputBonusPostPercentPowerOutputLocationShipGroupPowerCore(self, fitting, state = None, level = 1):
    boost(fitting.ship, "powerOutput", "powerEngineeringOutputBonus",
          self.item, extraMult = level)
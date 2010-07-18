#Items from group: Rig Energy Grid (6 of 30) [Module]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Engineering Implants (3 of 6)
#Item: Engineering [Skill]
from customEffects import boost
def engineeringPowerEngineeringOutputBonusPostPercentPowerOutputLocationShipGroupPowerCore(self, fitting, state = None, level = 1):
    boost(fitting.ship, "powerOutput", "powerEngineeringOutputBonus",
          self.item, extraMult = level)
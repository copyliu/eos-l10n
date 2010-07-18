#Items from group: Booster (4 of 34) [Implant]
#Items from group: Cyber Engineering (3 of 21) [Implant]
#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Management [Skill]
from customEffects import boost
def energyManagementCapacitorBonusPostPercentCapacityLocationShipGroupCapacitorCapacityBonus(self, fitting, state = None, level = 1):
    boost(fitting.ship, "capacitorCapacity", "capacitorCapacityBonus",
          self.item, extraMult = level)
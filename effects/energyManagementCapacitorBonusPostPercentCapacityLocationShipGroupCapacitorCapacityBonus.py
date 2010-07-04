#Used by: Skill: Energy Management
#         Item : Semiconductor Memory Cell
#                Mindflood Booster
from customEffects import boost
def energyManagementCapacitorBonusPostPercentCapacityLocationShipGroupCapacitorCapacityBonus(self, fitting, state = None, level = 1):
    boost(fitting.ship, "capacitorCapacity", "capacitorCapacityBonus",
          self.item, extraMult = level)
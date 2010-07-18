#Items from group: Sensor Booster Script (2 of 2) [Charge]
#Items from group: Sensor Dampener Script (2 of 2) [Charge]
from customEffects import boost
def scriptSensorBoosterMaxTargetRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxTargetRangeBonus", "maxTargetRangeBonusBonus", self.item)
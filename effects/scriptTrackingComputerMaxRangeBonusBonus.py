#Items from group: Tracking Disruption Script (2 of 2) [Charge]
#Items from group: Tracking Script (2 of 2) [Charge]
from customEffects import boost
def scriptTrackingComputerMaxRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxRangeBonus", "maxRangeBonusBonus", self.item)
    boost(containerModule, "falloffBonus", "falloffBonusBonus", self.item)

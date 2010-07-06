#Used by: Ammo: Tracking Computer Script
from customEffects import boost
def scriptTrackingComputerMaxRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxRangeBonus", "maxRangeBonusBonus", self.item)
    boost(containerModule, "falloffBonus", "falloffBonusBonus", self.item)

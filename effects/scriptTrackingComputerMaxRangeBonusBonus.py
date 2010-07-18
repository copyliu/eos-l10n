#Items from market group: Ammunition & Charges > Scripts (4 of 9)
from customEffects import boost
def scriptTrackingComputerMaxRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxRangeBonus", "maxRangeBonusBonus", self.item)
    boost(containerModule, "falloffBonus", "falloffBonusBonus", self.item)

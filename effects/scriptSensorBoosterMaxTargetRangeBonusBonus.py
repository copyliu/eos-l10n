#Items from market group: Ammunition & Charges > Scripts (4 of 9)
from customEffects import boost
def scriptSensorBoosterMaxTargetRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxTargetRangeBonus", "maxTargetRangeBonusBonus", self.item)
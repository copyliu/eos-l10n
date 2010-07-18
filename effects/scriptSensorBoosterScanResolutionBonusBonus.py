#Items from market group: Ammunition & Charges > Scripts (4 of 9)
from customEffects import boost
def scriptSensorBoosterScanResolutionBonusBonus(self, fitting, containerModule):
    boost(containerModule, "scanResolutionBonus", "scanResolutionBonusBonus", self.item)
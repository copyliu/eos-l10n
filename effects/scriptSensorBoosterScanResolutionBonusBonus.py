#Used by: Ammo: Scan Resolution
from customEffects import boost
def scriptSensorBoosterScanResolutionBonusBonus(self, fitting, containerModule):
    boost(containerModule, "scanResolutionBonus", "scanResolutionBonusBonus", self.item)
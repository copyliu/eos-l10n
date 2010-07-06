#Used by: Ammo: Scan Resolution
from customEffects import boost
def scriptSensorBoosterMaxTargetRangeBonusBonus(self, fitting, containerModule):
    boost(containerModule, "maxTargetRangeBonus", "maxTargetRangeBonusBonus", self.item)
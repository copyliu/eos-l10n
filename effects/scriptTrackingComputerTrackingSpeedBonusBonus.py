#Items from market group: Ammunition & Charges > Scripts (4 of 9)
from customEffects import boost
def scriptTrackingComputerTrackingSpeedBonusBonus(self, fitting, containerModule):
    boost(containerModule, "trackingSpeedBonus", "trackingSpeedBonusBonus", self.item)

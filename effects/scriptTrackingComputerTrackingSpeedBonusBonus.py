#Used by: Ammo: Tracking Computer Script
from customEffects import boost
def scriptTrackingComputerTrackingSpeedBonusBonus(self, fitting, containerModule):
    boost(containerModule, "trackingSpeedBonus", "trackingSpeedBonusBonus", self.item)

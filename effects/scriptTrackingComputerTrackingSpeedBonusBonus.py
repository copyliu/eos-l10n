#Items from group: Tracking Disruption Script (2 of 2) [Charge]
#Items from group: Tracking Script (2 of 2) [Charge]
from customEffects import boost
def scriptTrackingComputerTrackingSpeedBonusBonus(self, fitting, containerModule):
    boost(containerModule, "trackingSpeedBonus", "trackingSpeedBonusBonus", self.item)

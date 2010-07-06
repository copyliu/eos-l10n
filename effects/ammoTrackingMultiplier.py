#Used by: T2 ammo
from customEffects import multiply
def ammoTrackingMultiplier(self, fitting, containerModule):
    multiply(containerModule, "trackingSpeed", "trackingSpeedMultiplier", self.item)
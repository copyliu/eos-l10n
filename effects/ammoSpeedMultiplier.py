#Used by: All T2 ammo
from customEffects import multiply
def ammoSpeedMultiplier(self, fitting, containerModule):
    multiply(containerModule, "speed", "speedMultiplier", self.item)
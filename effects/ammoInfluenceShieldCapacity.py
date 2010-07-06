#Used by: T2 Ammo
from customEffects import multiply
def ammoInfluenceShieldCapacity(self, fitting, containerModule):
    multiply(fitting.ship, "shieldCapacity", "shieldCapacityMultiplier", self.item)
#Used by: T2 Ammo
from customEffects import multiply
def ammoFallofMultiplier(self, fitting, containerModule):
    multiply(containerModule, "falloff", "fallofMultiplier", self.item)
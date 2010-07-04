#Used by: All ammo
from customEffects import multiply
def ammoInfluenceRange(self, fitting, containerModule):
    multiply(containerModule, "maxRange", "weaponRangeMultiplier", self.item)
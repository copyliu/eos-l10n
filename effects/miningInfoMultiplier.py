#Items from market group: Ammunition & Charges > Mining Crystals (32 of 32)
from customEffects import multiply
def miningInfoMultiplier(self, fitting, containerModule):
    multiply(containerModule, "miningAmount", "specialisationAsteroidYieldMultiplier", self.item)

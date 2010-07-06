#Used by: Item: Mining Crystals Group
from customEffects import multiply
def miningInfoMultiplier(self, fitting, containerModule):
    multiply(containerModule, "miningAmount", "specialisationAsteroidYieldMultiplier", self.item)

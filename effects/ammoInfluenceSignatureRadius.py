#Used by: T2 Ammo
from customEffects import multiply
def ammoInfluenceSignatureRadius(self, fitting, containerModule):
    multiply(fitting.ship, "signatureRadius", "signatureRadiusMultiplier", self.item)
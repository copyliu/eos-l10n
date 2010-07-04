#Used by: Item: Halo Implants
#               X-Instinct Booster
from customEffects import boost
def structureStealthEmitterArraySigDecrease(self, fitting):
    boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
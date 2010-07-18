#Items from group: Cyberimplant (10 of 138) [Implant]
#Item: Improved X-Instinct Booster [Implant]
#Item: Standard X-Instinct Booster [Implant]
#Item: Strong X-Instinct Booster [Implant]
#Item: Synth X-Instinct Booster [Implant]
from customEffects import boost
def structureStealthEmitterArraySigDecrease(self, fitting):
    boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
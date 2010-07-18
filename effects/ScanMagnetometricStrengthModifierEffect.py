#Items from group: Cyberimplant (5 of 138)
from customEffects import increase
def ScanMagnetometricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanMagnetometricStrength",
             "scanMagnetometricStrengthModifier", self.item)
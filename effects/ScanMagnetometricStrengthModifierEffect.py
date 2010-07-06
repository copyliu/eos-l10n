#Used by: Item: Low-Grade Spur Set
from customEffects import increase
def ScanMagnetometricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanMagnetometricStrength",
             "scanMagnetometricStrengthModifier", self.item)
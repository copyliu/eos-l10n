#Item: Low-grade Spur Alpha [Implant]
#Item: Low-grade Spur Beta [Implant]
#Item: Low-grade Spur Delta [Implant]
#Item: Low-grade Spur Epsilon [Implant]
#Item: Low-grade Spur Gamma [Implant]
from customEffects import increase
def ScanMagnetometricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanMagnetometricStrength",
             "scanMagnetometricStrengthModifier", self.item)
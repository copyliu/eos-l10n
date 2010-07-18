#Item: Low-grade Talon Alpha [Implant]
#Item: Low-grade Talon Beta [Implant]
#Item: Low-grade Talon Delta [Implant]
#Item: Low-grade Talon Epsilon [Implant]
#Item: Low-grade Talon Gamma [Implant]
from customEffects import increase
def ScanGravimetricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanGravimetricStrength", "scanGravimetricStrengthModifier",
             self.item)
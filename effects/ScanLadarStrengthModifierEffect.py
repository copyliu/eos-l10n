#Item: Low-grade Jackal Alpha [Implant]
#Item: Low-grade Jackal Beta [Implant]
#Item: Low-grade Jackal Delta [Implant]
#Item: Low-grade Jackal Epsilon [Implant]
#Item: Low-grade Jackal Gamma [Implant]
from customEffects import increase
def ScanLadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanLadarStrength", "scanLadarStrengthModifier", self.item)
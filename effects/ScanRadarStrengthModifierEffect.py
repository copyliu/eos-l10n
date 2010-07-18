#Item: Low-grade Grail Alpha [Implant]
#Item: Low-grade Grail Beta [Implant]
#Item: Low-grade Grail Delta [Implant]
#Item: Low-grade Grail Epsilon [Implant]
#Item: Low-grade Grail Gamma [Implant]
from customEffects import increase
def ScanRadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanRadarStrength", "scanRadarStrengthModifier", self.item)
#Items from group: Cyberimplant (5 of 138) [Implant]
from customEffects import increase
def ScanRadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanRadarStrength", "scanRadarStrengthModifier", self.item)
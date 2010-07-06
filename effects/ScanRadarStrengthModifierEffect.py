#Used by: Item: Low-Grade Grail Set
from customEffects import increase
def ScanRadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanRadarStrength", "scanRadarStrengthModifier", self.item)
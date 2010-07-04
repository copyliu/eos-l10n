#Used by: Item: Low-Grade Talon Set
from customEffects import increase
def ScanGravimetricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanGravimetricStrength", "scanGravimetricStrengthModifier",
             self.item)
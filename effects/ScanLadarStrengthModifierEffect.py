#Used by: Item: Low-Grade Jackal Set
from customEffects import increase
def ScanLadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanLadarStrength", "scanLadarStrengthModifier", self.item)
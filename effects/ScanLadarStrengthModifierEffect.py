#Items from group: Cyberimplant (5 of 138) [Implant]
from customEffects import increase
def ScanLadarStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanLadarStrength", "scanLadarStrengthModifier", self.item)
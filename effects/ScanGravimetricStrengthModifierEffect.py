#Items from group: Cyberimplant (5 of 138) [Implant]
from customEffects import increase
def ScanGravimetricStrengthModifierEffect(self, fitting):
    increase(fitting.ship, "scanGravimetricStrength", "scanGravimetricStrengthModifier",
             self.item)
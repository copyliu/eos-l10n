#Used by: Item: Magnatar Effect Beacon
from customEffects import multiply
type = "projected"
def systemShieldKineticResistance(self, fitting, state):
    multiply(fitting.ship, "shieldKineticDamageResonance", "shieldKineticDamageResistanceBonus", self.item)
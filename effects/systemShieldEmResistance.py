#Used by: Item: Magnatar Effect Beacon
from customEffects import multiply
type = "projected"
def systemShieldEmResistance(self, fitting, state):
    multiply(fitting.ship, "shieldEmDamageResonance", "shieldEmDamageResistanceBonus", self.item)
#Used by: Item: Magnatar Effect Beacon
from customEffects import multiply
type = "projected"
def systemShieldExplosiveResistance(self, fitting, state):
    multiply(fitting.ship, "shieldExplosiveDamageResonance", "shieldExplosiveDamageResistanceBonus", self.item)
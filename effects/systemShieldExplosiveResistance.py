#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply
type = "projected"
def systemShieldExplosiveResistance(self, fitting, state):
    multiply(fitting.ship, "shieldExplosiveDamageResonance", "shieldExplosiveDamageResistanceBonus", self.item)
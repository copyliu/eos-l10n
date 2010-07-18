#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply
type = "projected"
def systemShieldKineticResistance(self, fitting, state):
    multiply(fitting.ship, "shieldKineticDamageResonance", "shieldKineticDamageResistanceBonus", self.item)
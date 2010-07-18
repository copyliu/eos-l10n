#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply
type = "projected"
def systemShieldEmResistance(self, fitting, state):
    multiply(fitting.ship, "shieldEmDamageResonance", "shieldEmDamageResistanceBonus", self.item)
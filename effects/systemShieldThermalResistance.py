#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply
type = "projected"
def systemShieldThermalResistance(self, fitting, state):
    multiply(fitting.ship, "shieldThermalDamageResonance", "shieldThermalDamageResistanceBonus", self.item)
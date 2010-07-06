#Used by: Item: Magnatar Effect Beacon
from customEffects import multiply
type = "projected"
def systemShieldThermalResistance(self, fitting, state):
    multiply(fitting.ship, "shieldThermalDamageResonance", "shieldThermalDamageResistanceBonus", self.item)
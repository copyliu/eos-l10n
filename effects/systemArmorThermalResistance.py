#Items from group: Effect Beacon (12 of 38) [Celestial]
type = "projected"
from customEffects import boost
def systemArmorThermalResistance(self, fitting, state):
    boost(fitting.ship, "armorThermalDamageResonance", "armorThermalDamageResistanceBonus", self.item)
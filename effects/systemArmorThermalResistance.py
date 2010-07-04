#Used by: Item: Pulsar Effect Beacon
#               Wolf Rayet Effect Beacon
type = "projected"
from customEffects import boost
def systemArmorThermalResistance(self, fitting, state):
    boost(fitting.ship, "armorThermalDamageResonance", "armorThermalDamageResistanceBonus", self.item)
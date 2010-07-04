#Used by: Item: Pulsar Effect Beacon
#               Wolf Rayet Effect Beacon
type = "projected"
from customEffects import boost
def systemArmorKineticResistance(self, fitting, state):
    boost(fitting.ship, "armorKineticDamageResonance", "armorKineticDamageResistanceBonus", self.item)
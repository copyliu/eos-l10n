#Used by: Item: Pulsar Effect Beacon
#               Wolf Rayet Effect Beacon
type = "projected"
from customEffects import boost
def systemArmorEmResistance(self, fitting, state):
    boost(fitting.ship, "armorEmDamageResonance", "armorEmDamageResistanceBonus", self.item)
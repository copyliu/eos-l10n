#Used by: Item: Pulsar Effect Beacon
#               Wolf Rayet Effect Beacon
type = "projected"
from customEffects import boost
def systemArmorExplosiveResistance(self, fitting, state):
    boost(fitting.ship, "armorExplosiveDamageResonance", "armorExplosiveDamageResistanceBonus", self.item)
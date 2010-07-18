#Items from group: Effect Beacon (12 of 38) [Celestial]
type = "projected"
from customEffects import boost
def systemArmorExplosiveResistance(self, fitting, state):
    boost(fitting.ship, "armorExplosiveDamageResonance", "armorExplosiveDamageResistanceBonus", self.item)
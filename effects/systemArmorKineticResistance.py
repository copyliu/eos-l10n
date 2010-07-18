#Items from group: Effect Beacon (12 of 38) [Celestial]
type = "projected"
from customEffects import boost
def systemArmorKineticResistance(self, fitting, state):
    boost(fitting.ship, "armorKineticDamageResonance", "armorKineticDamageResistanceBonus", self.item)
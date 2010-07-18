#Items from group: Effect Beacon (12 of 38)
type = "projected"
from customEffects import boost
def systemArmorEmResistance(self, fitting, state):
    boost(fitting.ship, "armorEmDamageResonance", "armorEmDamageResistanceBonus", self.item)
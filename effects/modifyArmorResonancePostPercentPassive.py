#Items from group: Rig Armor (24 of 54) [Module]
from customEffects import boost
def modifyArmorResonancePostPercentPassive(self, fitting, state):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        boost(fitting.ship, "armor" + damageType.capitalize() + "DamageResonance",
              damageType + "DamageResistanceBonus", self.item,
              useStackingPenalty = True)
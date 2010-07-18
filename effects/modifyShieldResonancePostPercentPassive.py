#Items from group: Rig Shield (24 of 54)
from customEffects import boost
def modifyShieldResonancePostPercentPassive(self, fitting, state):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        boost(fitting.ship, "shield" + damageType.capitalize() + "DamageResonance",
              damageType + "DamageResistanceBonus", self.item,
              useStackingPenalty = True)
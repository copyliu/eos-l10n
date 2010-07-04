#Used by: Item: Screen Reinforcer
#               Shield Resistance Amplifier
from customEffects import boost
def modifyShieldResonancePostPercentPassive(self, fitting, state):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        boost(fitting.ship, "shield" + damageType.capitalize() + "DamageResonance",
              damageType + "DamageResistanceBonus", self.item,
              useStackingPenalty = True)
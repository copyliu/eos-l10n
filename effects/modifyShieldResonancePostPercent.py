#Items from group: Shield Amplifier (88 of 88) [Module]
from customEffects import boost
import model.fitting

def modifyShieldResonancePostPercent(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boost(fitting.ship, "shield" + damageType.capitalize() + "DamageResonance",
                  damageType + "DamageResistanceBonus", self.item,
                  useStackingPenalty = True)

#Items from group: Shield Hardener (91 of 91) [Module]
import model.fitting
from customEffects import boost
runTime = "late"
type = "active"
def modifyActiveShieldResonanceAndNullifyPassiveResonance(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boost(fitting.ship, "shield" + damageType.capitalize() + "DamageResonance",
                  damageType + "DamageResistanceBonus",
                  self.item, useStackingPenalty = True)
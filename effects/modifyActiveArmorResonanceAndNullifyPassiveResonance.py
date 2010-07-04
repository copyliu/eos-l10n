#Used by: Item: Armor Hardeners
import model.fitting
from customEffects import boost
runTime = "late"
type = "active"
def modifyActiveArmorResonanceAndNullifyPassiveResonance(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boost(fitting.ship, "armor" + damageType.capitalize() + "DamageResonance",
                  damageType + "DamageResistanceBonus",
                  self.item, useStackingPenalty = True)
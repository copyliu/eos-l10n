#Used by: Item: Armor Plating
#               Energized Armor Plating
from customEffects import boost
import model.fitting

def modifyArmorResonancePostPercent(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boost(fitting.ship, "armor" + damageType.capitalize() + "DamageResonance",
                  damageType + "DamageResistanceBonus", self.item,
                  useStackingPenalty = True)

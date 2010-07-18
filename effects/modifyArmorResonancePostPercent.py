#Items from group: Armor Coating (201 of 201)
#Items from group: Armor Plating Energized (187 of 187)
from customEffects import boost
import model.fitting

def modifyArmorResonancePostPercent(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boost(fitting.ship, "armor" + damageType.capitalize() + "DamageResonance",
                  damageType + "DamageResistanceBonus", self.item,
                  useStackingPenalty = True)

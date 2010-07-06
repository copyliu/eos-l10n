#Used by: Item: Anti-EM Pump 
#               Anti-Explosive Pump
#               Anti-Kinetic Pump
#               Anti-Thermic Pump
from customEffects import boost
def modifyArmorResonancePostPercentPassive(self, fitting, state):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        boost(fitting.ship, "armor" + damageType.capitalize() + "DamageResonance",
              damageType + "DamageResistanceBonus", self.item,
              useStackingPenalty = True)
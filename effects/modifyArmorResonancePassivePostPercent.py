#Items from group: Armor Hardener (156 of 156) [Module]
import model.fitting
from customEffects import boost
def modifyArmorResonancePassivePostPercent(self, fitting, state):
    if state == model.fitting.STATE_INACTIVE:
        for damageType in ("Kinetic", "Thermal", "Explosive", "Em"):
            if damageType == "Thermal":
                dn = "Thermic"
            else:
                dn = damageType
                
            boost(fitting.ship, "armor" + damageType + "DamageResonance",
                  "passive" + dn + "DamageResistanceBonus", self.item,
                  useStackingPenalty = True)
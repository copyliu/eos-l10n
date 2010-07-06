#Used by: Item: Shield Hardener
import model.fitting
from customEffects import boost
def modifyShieldResonancePassivePostPercent(self, fitting, state):
    if state == model.fitting.STATE_INACTIVE:
        for damageType in ("Kinetic", "Thermal", "Explosive", "Em"):
            if damageType == "Thermal":
                dn = "Thermic"
            else:
                dn = damageType
                
            boost(fitting.ship, "shield" + damageType + "DamageResonance",
                  "passive" + dn + "DamageResistanceBonus", self.item,
                  useStackingPenalty = True)
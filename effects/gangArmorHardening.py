#Item: Armored Warfare Link - Passive Defense
import model.fitting
from customEffects import boost
type = ("gang", "active")

def gangArmorHardening(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(
            fitting.ship,
            (
                "armorEmDamageResonance",
                "armorThermalDamageResonance",
                "armorExplosiveDamageResonance",
                "armorKineticDamageResonance"
            ),
            "commandBonus",
            self.item,
            useStackingPenalty = True
        )

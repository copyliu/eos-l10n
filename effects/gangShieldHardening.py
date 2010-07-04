#Used by: Item: Siege Warfare Link - Shield Harmonizing
from customEffects import boost
import model.fitting
type = ("gang", "active")

def gangShieldHardening(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(
            fitting.ship,
            (
                "shieldEmDamageResonance",
                "shieldExplosiveDamageResonance",
                "shieldThermalDamageResonance",
                "shieldKineticDamageResonance"
            ),
            "commandBonus",
            self.item,
            useStackingPenalty = True
        )

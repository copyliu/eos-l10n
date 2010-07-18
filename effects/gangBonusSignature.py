#Item: Skirmish Warfare Link - Evasive Maneuvers [Module]
import model.fitting
from customEffects import boost
type = ("gang", "active")

def gangBonusSignature(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(
            fitting.ship,
            "signatureRadius",
            "commandBonus",
            self.item,
            useStackingPenalty = True
        )

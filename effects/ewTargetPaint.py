#Used by: Item: Target Painter
import model.fitting
from customEffects import boost
type = ("projected", "active")
def ewTargetPaint(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "signatureRadius", "signatureRadiusBonus",
              self.item, useStackingPenalty = True)
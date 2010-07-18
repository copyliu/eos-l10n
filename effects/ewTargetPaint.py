#Items from group: Electronic Warfare Drone (3 of 12) [Drone]
#Items from group: Target Painter (9 of 9) [Module]
import model.fitting
from customEffects import boost
type = ("projected", "active")
def ewTargetPaint(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "signatureRadius", "signatureRadiusBonus",
              self.item, useStackingPenalty = True)
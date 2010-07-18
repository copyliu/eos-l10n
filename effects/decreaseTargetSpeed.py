#Items from group: Stasis Web (19 of 19) [Module]
#Item: Berserker SW-900 [Drone]
import model.fitting
from customEffects import boost
type = ("projected", "active")
def decreaseTargetSpeed(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item, useStackingPenalty = True)

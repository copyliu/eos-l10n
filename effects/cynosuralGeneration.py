#Items from group: Cynosural Field (2 of 2) [Module]
from customEffects import boost
import model.fitting
type = 'active'
def cynosuralGeneration(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item)

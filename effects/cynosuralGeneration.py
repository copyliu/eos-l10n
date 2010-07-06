#Used by: Item: Cynosural Field Generator I
#               Covert Cynosural Field Generator I
from customEffects import boost
import model.fitting
type = 'active'
def cynosuralGeneration(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item)

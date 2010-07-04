#Used by: Item: Industrial Core I
import model.fitting
from customEffects import multiply, boost
type = "active"
def industrialCoreEffect2(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        #Speed bonus
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item)

        #Mass
        multiply(fitting.ship, "mass", "massMultiplier", self.item)

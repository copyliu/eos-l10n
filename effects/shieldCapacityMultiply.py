#Used by: Item: Power Diagnostic System
import model.fitting
from customEffects import multiply
def shieldCapacityMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "shieldCapacity", "shieldCapacityMultiplier", self.item)
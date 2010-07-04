#Used by: Item: Power Diagnostic System
import model.fitting
from customEffects import multiply
def powerOutputMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "powerOutput", "powerOutputMultiplier", self.item)
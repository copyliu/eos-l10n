#Used by: Item: Reinforced Bulkheads
#               Nanofiber Internal Structure
from customEffects import multiply
import model.fitting
def structureHPMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "hp", "structureHPMultiplier", self.item)
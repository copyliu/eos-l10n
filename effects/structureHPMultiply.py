#Items from group: Nanofiber Internal Structure (14 of 14)
#Items from group: Reinforced Bulkhead (12 of 12)
from customEffects import multiply
import model.fitting
def structureHPMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "hp", "structureHPMultiplier", self.item)
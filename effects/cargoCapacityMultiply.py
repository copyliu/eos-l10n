#Items from group: Expanded Cargohold (13 of 13)
#Items from group: Overdrive Injector System (14 of 14)
import model.fitting
from customEffects import multiply
def cargoCapacityMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "capacity", "cargoCapacityMultiplier", self.item)
#Used by: Item: Cargohold Expander
#               Overdrive Injector System
import model.fitting
from customEffects import multiply
def cargoCapacityMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "capacity", "cargoCapacityMultiplier", self.item)
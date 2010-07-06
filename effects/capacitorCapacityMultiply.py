#Used by: Item: Capacitor Flux Coil
#               Power Diagnostic System
#               MicroWarpdrive
import model.fitting
from customEffects import multiply
def capacitorCapacityMultiply(self, fitting, state):
    if self.item.group.name != "Afterburner" or state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "capacitorCapacity", "capacitorCapacityMultiplier",
                 self.item)
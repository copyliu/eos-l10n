#Items from group: Afterburner (107 of 107) [Module]
#Items from group: Capacitor Flux Coil (12 of 12) [Module]
#Items from group: Capacitor Power Relay (25 of 25) [Module]
#Items from group: Power Diagnostic System (31 of 31) [Module]
#Items from group: Reactor Control Unit (28 of 28) [Module]
#Items from group: Shield Flux Coil (11 of 11) [Module]
#Items from group: Shield Power Relay (11 of 11) [Module]
import model.fitting
from customEffects import multiply
def capacitorCapacityMultiply(self, fitting, state):
    if self.item.group.name != "Afterburner" or state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "capacitorCapacity", "capacitorCapacityMultiplier",
                 self.item)
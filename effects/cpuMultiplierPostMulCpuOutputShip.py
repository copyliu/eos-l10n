#Items from group: CPU Enhancer (27 of 27) [Module]
import model.fitting
from customEffects import multiply
def cpuMultiplierPostMulCpuOutputShip(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "cpuOutput", "cpuMultiplier", self.item)
#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import multiply
def systemDroneControlRange(self, fitting, state):
    multiply(fitting.ship, "_droneControlRange", "droneRangeMultiplier", self.item)
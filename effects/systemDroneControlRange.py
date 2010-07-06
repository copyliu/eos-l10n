#Used by: Item: Black Hole Effect Beacon
type = "projected"
from customEffects import multiply
def systemDroneControlRange(self, fitting, state):
    multiply(fitting.ship, "_droneControlRange", "droneRangeMultiplier", self.item)
#Used by: Item: Pulsar Effect Beacon
#               Magnetar Effect Beacon
type = "projected"
from customEffects import multiply
def systemTargetingRange(self, fitting, state):
    multiply(fitting.ship, "maxTargetRange", "maxTargetRangeMultiplier", self.item)
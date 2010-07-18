#Items from group: Effect Beacon (12 of 38)
type = "projected"
from customEffects import multiply
def systemTargetingRange(self, fitting, state):
    multiply(fitting.ship, "maxTargetRange", "maxTargetRangeMultiplier", self.item)
#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import multiply
type = "projected"
def systemMaxVelocity(self, fitting, state):
    multiply(fitting.ship, "maxVelocity", "maxVelocityMultiplier", self.item)
#Used by: Item: Black Hole Effect Beacon
from customEffects import multiply
type = "projected"
def systemMaxVelocity(self, fitting, state):
    multiply(fitting.ship, "maxVelocity", "maxVelocityMultiplier", self.item)
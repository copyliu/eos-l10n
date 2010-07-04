#Used by: Item: Pulsar Effect Beacon
from customEffects import multiply
type = "projected"
def systemShieldHP(self, fitting, state):
    multiply(fitting.ship, "shieldCapacity", "shieldCapacityMultiplier", self.item)
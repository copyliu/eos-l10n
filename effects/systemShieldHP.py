#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply
type = "projected"
def systemShieldHP(self, fitting, state):
    multiply(fitting.ship, "shieldCapacity", "shieldCapacityMultiplier", self.item)
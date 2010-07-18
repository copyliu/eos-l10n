#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import multiply
def systemCapacitorCapacity(self, fitting, state):
    multiply(fitting.ship, "capacitorCapacity", "capacitorCapacityMultiplierSystem", self.item)
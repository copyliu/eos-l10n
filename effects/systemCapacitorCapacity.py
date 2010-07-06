#Used by: Item: Cataclysmic Variable Effect Beacon
type = "projected"
from customEffects import multiply
def systemCapacitorCapacity(self, fitting, state):
    multiply(fitting.ship, "capacitorCapacity", "capacitorCapacityMultiplierSystem", self.item)
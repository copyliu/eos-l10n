#Used by: Item: Engineering subsystems
runTime = "early"
from customEffects import increase
def capacitorCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "capacitorCapacity", "capacitorCapacity",
             self.item, position = "pre")
#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def droneCapacityAdddroneCapacityPassive(self, fitting, state):
    increase(fitting.ship, "droneCapacity", "droneCapacity",
             self.item, position = "pre")
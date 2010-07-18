#Items from category: Subsystem (42 of 80)
runTime = "early"
from customEffects import increase
def droneCapacityAdddroneCapacityPassive(self, fitting, state):
    increase(fitting.ship, "droneCapacity", "droneCapacity",
             self.item, position = "pre")
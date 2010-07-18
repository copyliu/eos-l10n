#Items from category: Subsystem (17 of 80)
#Items from group: Engineering Systems (16 of 16)
runTime = "early"
from customEffects import increase
def capacitorCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "capacitorCapacity", "capacitorCapacity",
             self.item, position = "pre")
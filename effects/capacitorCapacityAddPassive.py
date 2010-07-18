#Items from group: Engineering Systems (16 of 16) [Subsystem]
#Item: Tengu Offensive - Magnetic Infusion Basin [Subsystem]
runTime = "early"
from customEffects import increase
def capacitorCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "capacitorCapacity", "capacitorCapacity",
             self.item, position = "pre")
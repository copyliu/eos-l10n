#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def shieldCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "shieldCapacity", "shieldCapacity",
             self.item, position = "pre")
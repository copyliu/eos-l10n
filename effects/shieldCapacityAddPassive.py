#Items from group: Defensive Systems (16 of 16)
runTime = "early"
from customEffects import increase
def shieldCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "shieldCapacity", "shieldCapacity",
             self.item, position = "pre")
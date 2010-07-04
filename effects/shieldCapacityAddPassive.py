#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def shieldCapacityAddPassive(self, fitting, state):
    increase(fitting.ship, "shieldCapacity", "shieldCapacity",
             self.item, position = "pre")
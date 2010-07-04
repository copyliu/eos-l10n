#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def capacityAddPassive(self, fitting, state):
    increase(fitting.ship, "capacity", "capacity", self.item, position = "pre")
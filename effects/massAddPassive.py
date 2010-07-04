#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def massAddPassive(self, fitting, state):
    increase(fitting.ship, "mass", "mass", self.item, position = "pre")
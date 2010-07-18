#Items from group: Defensive Systems (16 of 16)
runTime = "early"
from customEffects import increase
def capacityAddPassive(self, fitting, state):
    increase(fitting.ship, "capacity", "capacity", self.item, position = "pre")
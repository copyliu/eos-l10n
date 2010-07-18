#Items from category: Subsystem (80 of 80)
runTime = "early"
from customEffects import increase
def massAddPassive(self, fitting, state):
    increase(fitting.ship, "mass", "mass", self.item, position = "pre")
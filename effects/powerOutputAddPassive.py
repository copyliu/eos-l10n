#Items from category: Subsystem (40 of 80)
runTime = "early"
from customEffects import increase
def powerOutputAddPassive(self, fitting, state):
    increase(fitting.ship, "powerOutput", "powerOutput", self.item, position = "pre")
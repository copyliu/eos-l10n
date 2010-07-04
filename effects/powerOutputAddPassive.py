#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def powerOutputAddPassive(self, fitting, state):
    increase(fitting.ship, "powerOutput", "powerOutput", self.item, position = "pre")
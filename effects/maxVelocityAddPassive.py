#Used by: Item: All propulsion subsystems
runTime = "early"
from customEffects import increase
def maxVelocityAddPassive(self, fitting, state):
    increase(fitting.ship, "maxVelocity", "maxVelocity", self.item,
             position = "pre")
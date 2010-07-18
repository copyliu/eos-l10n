#Items from group: Propulsion Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def maxVelocityAddPassive(self, fitting, state):
    increase(fitting.ship, "maxVelocity", "maxVelocity", self.item,
             position = "pre")
#Items from group: Electronic Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def scanResolutionAddPassive(self, fitting, state):
    increase(fitting.ship, "scanResolution", "scanResolution",
             self.item, position = "pre")
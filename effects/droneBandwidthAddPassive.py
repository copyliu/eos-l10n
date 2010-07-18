#Items from category: Subsystem (29 of 80)
runTime = "early"
from customEffects import increase
def droneBandwidthAddPassive(self, fitting, state):
    increase(fitting.ship, "droneBandwidth", "droneBandwidth",
             self.item, position = "pre")
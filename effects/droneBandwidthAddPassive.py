#Items from group: Engineering Systems (13 of 16) [Subsystem]
#Items from group: Offensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def droneBandwidthAddPassive(self, fitting, state):
    increase(fitting.ship, "droneBandwidth", "droneBandwidth",
             self.item, position = "pre")
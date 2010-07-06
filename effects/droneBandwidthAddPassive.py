#Used by: Item: All offensive and engineering subsystems
runTime = "early"
from customEffects import increase
def droneBandwidthAddPassive(self, fitting, state):
    increase(fitting.ship, "droneBandwidth", "droneBandwidth",
             self.item, position = "pre")
#Items from group: Rig Drones (48 of 48) [Module]
from customEffects import boost
def drawbackCPUOutput(self, fitting, state):
    boost(fitting.ship, "cpuOutput", "drawback", self.item)
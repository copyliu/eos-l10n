#Used by: Item: All drone rigs
from customEffects import boost
def drawbackCPUOutput(self, fitting, state):
    boost(fitting.ship, "cpuOutput", "drawback", self.item)
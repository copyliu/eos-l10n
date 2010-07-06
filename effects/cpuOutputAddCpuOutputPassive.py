#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def cpuOutputAddCpuOutputPassive(self, fitting, state):
    increase(fitting.ship, "cpuOutput", "cpuOutput", self.item, position = "pre")
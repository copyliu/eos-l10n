#Items from category: Subsystem (40 of 80)
runTime = "early"
from customEffects import increase
def cpuOutputAddCpuOutputPassive(self, fitting, state):
    increase(fitting.ship, "cpuOutput", "cpuOutput", self.item, position = "pre")
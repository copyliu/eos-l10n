#Used by: Item: All Electronics subsystems
runTime = "early"
from customEffects import increase
def maxTargetRangeAddPassive(self, fitting, state):
    increase(fitting.ship, "maxTargetRange", "maxTargetRange", self.item,
             position = "pre")
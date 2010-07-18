#Items from group: Electronic Systems (16 of 16)
runTime = "early"
from customEffects import increase
def maxTargetRangeAddPassive(self, fitting, state):
    increase(fitting.ship, "maxTargetRange", "maxTargetRange", self.item,
             position = "pre")
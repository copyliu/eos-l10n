#Used by: Item: All Electronics T3 subsystems
runTime = "early"
from customEffects import increase
def scanResolutionAddPassive(self, fitting, state):
    increase(fitting.ship, "scanResolution", "scanResolution",
             self.item, position = "pre")
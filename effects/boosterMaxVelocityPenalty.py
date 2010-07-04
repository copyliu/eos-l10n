#Used by: Item: Crash Booster
#               Frentix Booster
#               Drop Booster
type = "boosterSideEffect"
from customEffects import boost
def boosterMaxVelocityPenalty(self, fitting):
    boost(fitting.ship, "maxVelocity", "boosterMaxVelocityPenalty", self.item)
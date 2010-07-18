#Item: Leadership
from customEffects import boost
type = "gang"
def leadershipEffect(self, fitting, level):
    boost(fitting.ship, "scanResolution", "scanResolutionBonus",
          self.item, extraMult = level)
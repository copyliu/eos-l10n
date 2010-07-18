#Items from group: Rig Electronics Superiority (3 of 48) [Module]
from customEffects import multiply
def scanResolutionBonusMultiplierPreMulPassive(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

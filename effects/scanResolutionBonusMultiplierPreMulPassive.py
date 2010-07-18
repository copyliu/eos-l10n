#Item: Large Targeting System Subcontroller II [Module]
#Item: Medium Targeting System Subcontroller II [Module]
#Item: Small Targeting System Subcontroller II [Module]
from customEffects import multiply
def scanResolutionBonusMultiplierPreMulPassive(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

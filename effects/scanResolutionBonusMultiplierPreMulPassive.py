#Used by: Item: Targeting System Subcontroller II
from customEffects import multiply
def scanResolutionBonusMultiplierPreMulPassive(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

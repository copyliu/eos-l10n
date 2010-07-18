#Items from group: Cloaking Device (12 of 14) [Module]
#Item: Large Targeting System Subcontroller I [Module]
#Item: Medium Targeting System Subcontroller I [Module]
#Item: Small Targeting System Subcontroller I [Module]
from customEffects import multiply
def cloakingScanResolutionMultiplier(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

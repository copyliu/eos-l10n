#Used by: Item: Targeting System Subcontroller I
#               Cloaking Devices
from customEffects import multiply
def cloakingScanResolutionMultiplier(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

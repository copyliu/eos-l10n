#Items from group: Cloaking Device (12 of 14) [Module]
#Items from group: Rig Electronics Superiority (3 of 48) [Module]
from customEffects import multiply
def cloakingScanResolutionMultiplier(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

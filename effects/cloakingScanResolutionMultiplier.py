#Items from group: Cloaking Device (12 of 14)
#Items from group: Rig Electronics Superiority (3 of 48)
from customEffects import multiply
def cloakingScanResolutionMultiplier(self, fitting, state):
    multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier",
             self.item, useStackingPenalty = True)

#Items from group: Warp Core Stabilizer (8 of 8) [Module]
from customEffects import multiply
import model.fitting
def scanResolutionMultiplierOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier", self.item, useStackingPenalty = True)
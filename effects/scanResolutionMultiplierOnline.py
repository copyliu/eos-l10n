#Used by: Item: Warp Core Stabilizer
from customEffects import multiply
import model.fitting
def scanResolutionMultiplierOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier", self.item, useStackingPenalty = True)
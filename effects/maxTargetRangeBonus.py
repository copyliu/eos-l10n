#Items from group: Warp Core Stabilizer (8 of 8) [Module]
from customEffects import boost
import model.fitting
def maxTargetRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, useStackingPenalty = True)

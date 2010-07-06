#Used by: Item: Warp Core Stabilizer
from customEffects import boost
import model.fitting
def maxTargetRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, useStackingPenalty = True)

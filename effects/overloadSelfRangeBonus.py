#Used by: Item: Warp Scrambler
#               Warp Disruptor
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "maxRange", "overloadRangeBonus", self.item, useStackingPenalty = True)

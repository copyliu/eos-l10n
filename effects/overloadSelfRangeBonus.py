#Items from group: Stasis Web (19 of 19)
#Items from group: Warp Scrambler (38 of 39)
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "maxRange", "overloadRangeBonus", self.item, useStackingPenalty = True)

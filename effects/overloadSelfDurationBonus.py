#Used by: Item: Hull Repairer
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "duration", "overloadSelfDurationBonus", self.item)
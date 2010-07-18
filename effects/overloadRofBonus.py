#Items from category: Module (372 of 3488)
from customEffects import boost
import model.fitting
type = "overload"
def overloadRofBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "speed", "overloadRofBonus", self.item)
#Items from group: Shield Booster (86 of 86) [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfShieldBonusDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "duration", "overloadSelfDurationBonus", self.item)
        boost(self.item, "shieldBonus", "overloadShieldBonus", self.item)
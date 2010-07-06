#Used by: Item: Turrets
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfDamageBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "damageMultiplier", "overloadDamageModifier", self.item)
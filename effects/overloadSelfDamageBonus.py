#Items from group: Energy Weapon (82 of 181)
#Items from group: Hybrid Weapon (88 of 197)
#Items from group: Projectile Weapon (82 of 141)
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfDamageBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "damageMultiplier", "overloadDamageModifier", self.item)
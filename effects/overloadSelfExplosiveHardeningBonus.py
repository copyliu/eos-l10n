#Items from group: Armor Hardener (39 of 156) [Module]
#Items from group: Shield Hardener (20 of 91) [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfExplosiveHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "explosiveDamageResistanceBonus", "overloadHardeningBonus", self.item)
#Items from group: Armor Hardener (39 of 156)
#Items from group: Shield Hardener (20 of 91)
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfEmHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "emDamageResistanceBonus", "overloadHardeningBonus", self.item)
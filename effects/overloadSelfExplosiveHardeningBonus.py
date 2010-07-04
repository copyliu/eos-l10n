#Used by: Item: Armor Explosive Hardener
#               Explosion Dampening field
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfExplosiveHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "explosiveDamageResistanceBonus", "overloadHardeningBonus", self.item)
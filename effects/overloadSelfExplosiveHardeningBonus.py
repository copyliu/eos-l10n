#Variations of item: Armor Explosive Hardener I (39 of 39) [Module]
#Variations of item: Explosion Dampening Field I (19 of 19) [Module]
#Item: Civilian Explosion Dampening Field [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfExplosiveHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "explosiveDamageResistanceBonus", "overloadHardeningBonus", self.item)
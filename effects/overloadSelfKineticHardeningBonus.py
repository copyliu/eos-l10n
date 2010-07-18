#Variations of item: Armor Kinetic Hardener I (39 of 39) [Module]
#Variations of item: Ballistic Deflection Field I (19 of 19) [Module]
#Item: Civilian Ballistic Deflection Field [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfKineticHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "kineticDamageResistanceBonus", "overloadHardeningBonus", self.item)
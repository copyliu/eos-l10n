#Used by: Item: Armor Thermal Hardener
#               Ballistic Deflection Field
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfKineticHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "kineticDamageResistanceBonus", "overloadHardeningBonus", self.item)
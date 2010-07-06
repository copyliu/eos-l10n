#Used by: Item: Armor Thermal Hardener
#               Heat Disipation Field
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfThermalHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "thermalDamageResistanceBonus", "overloadHardeningBonus", self.item)
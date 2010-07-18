#Variations of item: Armor Thermic Hardener I (39 of 39) [Module]
#Variations of item: Heat Dissipation Field I (19 of 19) [Module]
#Item: Civilian Heat Dissipation Field [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfThermalHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "thermalDamageResistanceBonus", "overloadHardeningBonus", self.item)
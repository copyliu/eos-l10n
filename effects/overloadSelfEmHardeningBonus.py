#Variations of item: Armor EM Hardener I (39 of 39) [Module]
#Variations of item: Photon Scattering Field I (19 of 19) [Module]
#Item: Civilian Photon Scattering Field [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfEmHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "emDamageResistanceBonus", "overloadHardeningBonus", self.item)
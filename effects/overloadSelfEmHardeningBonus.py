#Used by: Item: Armor EM Hardener
#               Photon Scattering Field
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfEmHardeningBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "emDamageResistanceBonus", "overloadHardeningBonus", self.item)
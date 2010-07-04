#Used by: Item: Armor Repairers
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfArmorDamageAmountDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "duration", "overloadSelfDurationBonus", self.item)
        boost(self.item, "armorDamageAmount", "overloadArmorDamageAmount", self.item)
#Used by: Cloaking devices
import model.fitting
from model.attribute import basicAttribute
from customEffects import multiply
type = "active"
def cloaking(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        fitting.ship.attributes["_cloaked"] = basicAttribute(fitting.ship, "_cloaked", None, True)
        velExtraMult = fitting.ship.getModifiedAttribute("_cloakedVelocityMultiplier") or 1
        multiply(fitting.ship, "maxVelocity", "maxVelocityBonus", self.item,
                 extraMult = velExtraMult)
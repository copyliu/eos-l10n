#Items from group: Cloaking Device (2 of 14) [Module]
import model.fitting
from model.attribute import basicAttribute
from customEffects import multiply
type = "active"
def cloakingWarpSafe(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        fitting.ship.attributes["_cloaked"] = basicAttribute(fitting.ship, "_cloaked", None, True)
        multiply(fitting.ship, "maxVelocity", "maxVelocityBonus", self.item)
#Used by: Item: Warp Disruption Field Generator
from customEffects import boost, boostModListByReq
import model.fitting
from model.attribute import basicAttribute
type = "active"
def warpDisruptSphere(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
        boostModListByReq(fitting.modules, "speedFactor", "speedFactorBonus",
                          lambda mod: mod.group.name == "Afterburner", self.item)
        fitting.ship.attributes["_disallowAssistance"] = \
            basicAttribute(fitting.ship, "_disallowAssistance", None, True)
        self.item.attributes["_maxRange"] = self.item.attributes["warpScrambleRange"]
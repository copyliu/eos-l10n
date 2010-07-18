#Items from group: Afterburner (53 of 107)
from customEffects import boost, increase
import model.fitting
runTime = "late"
type = "active"
def speedBoostMassSigRad(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        increase(fitting.ship, "mass", "massAddition", self.item)
        mass = fitting.ship.getModifiedAttribute("mass")
        thrust = float(self.item.getModifiedAttribute("speedBoostFactor"))
        boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item, extraMult = thrust / mass)
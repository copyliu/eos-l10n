#Items from group: Logistic Drone (6 of 12)
#Items from group: Shield Transporter (38 of 38)
import model.fitting
from customEffects import increase
type = ("projected", "active")
def shieldTransfer(self, fitting, state, activeLayer):
    self.item.attributes["_maxRange"] = self.item.attributes["shieldTransferRange"]
    if state >= model.fitting.STATE_ACTIVE and activeLayer == "projected" and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        shieldBonus = self.item.getModifiedAttribute("shieldBonus")
        duration = self.item.getModifiedAttribute("duration") / 1000.0
        shieldBonus = shieldBonus / duration
        increase(fitting.ship, "_shieldRawRecharge", shieldBonus)

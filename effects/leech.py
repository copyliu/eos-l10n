#Items from group: Energy Vampire (52 of 52)
from customEffects import increase
from model.attribute import basicAttribute
import model.fitting
type = ("active", "projected", "normal")
def leech(self, fitting, state, activeLayer):
    self.item.attributes["maxRange"] = self.item.attributes["powerTransferRange"]
    if state >= model.fitting.STATE_ACTIVE:
        amount = self.item.getModifiedAttribute("powerTransferAmount")
        time = self.item.getModifiedAttribute("duration") / 1000.0
        if activeLayer == "module":
            self.item.attributes["_capBoost"] = basicAttribute(self.item, "_capBoost", None, amount / time, 1)
        elif activeLayer == "projected" and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
            drain = -amount / time
            if not "_drain" in fitting.ship.attributes:
                fitting.ship.attributes["_drain"] = basicAttribute(self.item, "_drain", None, drain, 0)
            else:
                increase(fitting.ship, "_drain", drain)
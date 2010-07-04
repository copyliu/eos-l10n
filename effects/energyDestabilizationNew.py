#Used by: Energy Neutralizers
from customEffects import increase
import model.fitting
type = ("active", "projected", "normal")
def energyDestabilizationNew(self, fitting, state, activeLayer):
    self.item.attributes["maxRange"] = self.item.attributes["energyDestabilizationRange"]
    if activeLayer == "projected" and state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        amount = self.item.getModifiedAttribute("energyDestabilizationAmount")
        time = self.item.getModifiedAttribute("duration") / 1000.0
        drain = -amount / time
        increase(fitting.ship, "_drain", drain)
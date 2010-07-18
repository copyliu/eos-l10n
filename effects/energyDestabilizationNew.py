#Items from group: Cap Drain Drone (3 of 3) [Drone]
#Items from group: Energy Destabilizer (41 of 41) [Module]
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
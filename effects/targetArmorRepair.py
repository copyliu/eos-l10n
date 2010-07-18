#Items from group: Armor Repair Projector (37 of 37) [Module]
#Items from group: Logistic Drone (6 of 12) [Drone]
#Items from market group: Ship Equipment > Hull & Armor  > Remote Armor Repair Systems (19 of 19)
import model.fitting
from customEffects import increase
type = ("projected", "active")
def targetArmorRepair(self, fitting, state, activeLayer):
    if state >= model.fitting.STATE_ACTIVE and activeLayer == "projected" and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        armorAmount = self.item.getModifiedAttribute("armorDamageAmount")
        duration = self.item.getModifiedAttribute("duration") / 1000.0
        armorBonus = armorAmount / duration
        increase(fitting.ship, "_armorRawRecharge", armorBonus)

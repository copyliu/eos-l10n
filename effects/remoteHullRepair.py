#Used by: Item: Remote Hull Repairer
import model.fitting
from customEffects import increase
type = ("projected", "active")
def remoteHullRepair(self, fitting, state, activeLayer):
    if state >= model.fitting.STATE_ACTIVE and activeLayer == "projected" and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        structureAmount = self.item.getModifiedAttribute("structureDamageAmount")
        duration = self.item.getModifiedAttribute("duration") / 1000.0
        structureBonus = structureAmount / duration
        increase(fitting.ship, "_structureRawRecharge", structureBonus)

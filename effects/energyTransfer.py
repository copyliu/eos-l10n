#Items from group: Energy Transfer Array (37 of 37)
type = ("projected","active")
from customEffects import increase
def energyTransfer(self, fitting, state, activeLayer):
    self.item.attributes["_maxRange"] = self.item.attributes["powerTransferRange"]
    if activeLayer == "projected" and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        amount = self.item.getModifiedAttribute("powerTransferAmount")
        duration = self.item.getModifiedAttribute("duration") / 1000.0
        boostPerSec = amount / duration
        increase(fitting.ship, "_capBoost", boostPerSec)

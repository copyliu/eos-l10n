#Used by: Item: Capacitor Booster
import model.fitting
from model import attribute
runTime = "late"
type = "active"
def powerBooster(self, fitting, state):
    if self.item.ammo:
        boostAmount = self.item.ammo.getModifiedAttribute("capacitorBonus")
        rate = self.item.getModifiedAttribute("duration") / 1000.0
        chargeSize = self.item.ammo.getModifiedAttribute("volume")
        boosterSize = self.item.getModifiedAttribute("capacity")
        numBoostsTillEmpty = int(boosterSize / chargeSize)
        fullCycleTime = numBoostsTillEmpty * rate + 10
        fullCycleAmount = numBoostsTillEmpty * boostAmount
        boostPerSecond = fullCycleAmount / fullCycleTime            
        self.item.attributes["_capBoost"] = attribute.basicAttribute(self.item, "_capBoost", None, boostPerSecond, 1)

#Items from group: Capacitor Booster (54 of 54)
import model.fitting
from model import attribute
runTime = "late"
type = "active"
def powerBooster(self, fitting, state):
    if self.item.charge:
        boostAmount = self.item.charge.getModifiedAttribute("capacitorBonus")
        rate = self.item.getModifiedAttribute("duration") / 1000.0
        chargeSize = self.item.charge.getModifiedAttribute("volume")
        boosterSize = self.item.getModifiedAttribute("capacity")
        numBoostsTillEmpty = int(boosterSize / chargeSize)
        fullCycleTime = numBoostsTillEmpty * rate + 10
        fullCycleAmount = numBoostsTillEmpty * boostAmount
        boostPerSecond = fullCycleAmount / fullCycleTime            
        self.item.attributes["_capBoost"] = attribute.basicAttribute(self.item, "_capBoost", None, boostPerSecond, 1)

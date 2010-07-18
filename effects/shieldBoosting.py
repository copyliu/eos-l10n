#Items from group: Shield Booster (86 of 86) [Module]
runTime = "late"
from model import attribute
import model.fitting
type = "active"
def shieldBoosting(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        amount = self.item.getModifiedAttribute("shieldBonus")
        speed = self.item.getModifiedAttribute("duration") / 1000.0
        repairAmount = amount / speed
        self.item.attributes["_shieldRawRecharge"] = attribute.basicAttribute(self.item, "_shieldRawRecharge",
                                                                     None, repairAmount, 1)
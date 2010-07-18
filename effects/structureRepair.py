#Items from group: Hull Repair Unit (21 of 21)
runTime = "late"
from model import attribute
import model.fitting
type = "active"
def structureRepair(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        amount = self.item.getModifiedAttribute("structureDamageAmount")
        speed = self.item.getModifiedAttribute("duration") / 1000.0
        repairAmount = amount / speed
        self.item.attributes["_hullRawRecharge"] = attribute.basicAttribute(self.item, "_hullRawRecharge",
                                                                     None, repairAmount, 1)
#Used by: Item: Armor Repairer
runTime = "late"
type = "active"
from model import attribute
import model.fitting
def armorRepair(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        amount = self.item.getModifiedAttribute("armorDamageAmount")
        speed = self.item.getModifiedAttribute("duration") / 1000.0
        repairAmount = amount / speed
        self.item.attributes["_armorRawRecharge"] = attribute.basicAttribute(self.item, "_armorRawRecharge",
                                                                             None, repairAmount, 1)
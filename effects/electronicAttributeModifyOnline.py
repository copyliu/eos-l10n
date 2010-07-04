#Used by: Item: Auto Targeting Systems
from customEffects import increase
import model.fitting
type = "active"
def electronicAttributeModifyOnline(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        increase(fitting.ship, "maxLockedTargets", "maxLockedTargetsBonus", self.item)
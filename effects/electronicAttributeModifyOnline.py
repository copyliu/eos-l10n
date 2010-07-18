#Items from group: Automated Targeting System (6 of 6) [Module]
from customEffects import increase
import model.fitting
type = "active"
def electronicAttributeModifyOnline(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        increase(fitting.ship, "maxLockedTargets", "maxLockedTargetsBonus", self.item)
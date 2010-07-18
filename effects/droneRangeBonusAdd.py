#Items from group: Drone Control Range Module (2 of 2) [Module]
from customEffects import increase
import model.fitting
def droneRangeBonusAdd(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "_droneControlRange", "droneRangeBonus", self.item)
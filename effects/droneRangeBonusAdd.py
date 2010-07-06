#Used by: Item: Drone Link Augmentor
from customEffects import increase
import model.fitting
def droneRangeBonusAdd(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "_droneControlRange", "droneRangeBonus", self.item)
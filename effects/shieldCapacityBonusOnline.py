#Used by: Item: Shield Extender
import model.fitting
from customEffects import increase
runTime = "early"
def shieldCapacityBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "shieldCapacity", "capacityBonus", self.item,
                 position = "pre")
#Items from group: Shield Amplifier (88 of 88) [Module]
#Items from group: Shield Extender (37 of 37) [Module]
import model.fitting
from customEffects import increase
runTime = "early"
def shieldCapacityBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "shieldCapacity", "capacityBonus", self.item,
                 position = "pre")
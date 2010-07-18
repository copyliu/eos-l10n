#Items from group: Auxiliary Power Core (7 of 7) [Module]
import model.fitting
from customEffects import increase
runTime = "early"
def powerIncrease(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "powerOutput", "powerIncrease",
                 self.item, position = "pre")
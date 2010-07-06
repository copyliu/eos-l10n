#Used by: Item: Capacitor batteries
import model.fitting
from customEffects import increase
def capacitorCapacityBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "capacitorCapacity", "capacitorBonus", self.item)

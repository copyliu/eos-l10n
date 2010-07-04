#Used by: Item: Armor Plates
import model.fitting
from customEffects import increase
def armorReinforcerMassAdd(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "mass", "massAddition", self.item)

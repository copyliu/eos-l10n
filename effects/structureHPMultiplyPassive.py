#Used by: Item: Cargo hold Expanders
from customEffects import multiply
import model.fitting
def structureHPMultiplyPassive(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "hp", "structureHPMultiplier", self.item)
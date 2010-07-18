#Items from group: Expanded Cargohold (13 of 13) [Module]
from customEffects import multiply
import model.fitting
def structureHPMultiplyPassive(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "hp", "structureHPMultiplier", self.item)
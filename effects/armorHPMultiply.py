#Used by: Regenerative Plating
from customEffects import multiply
import model.fitting

def armorHPMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "armorHP", "armorHPMultiplier", self.item)

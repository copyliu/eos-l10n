#Used by: Reinforced Bulkheads
import model.fitting
from customEffects import multiply
def modifyMaxVelocityOfShipOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "maxVelocity", "maxVelocityBonus",
                 self.item, useStackingPenalty = True)
#Used by: Cargo hold Expanders
from customEffects import multiply
import model.fitting
def modifyMaxVelocityOfShipPassive(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "maxVelocity", "maxVelocityBonus",
                 self.item, useStackingPenalty = True)
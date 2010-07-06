#Used by: Item: Nanofiber Internal Structure
#               Reinforced Bulkheads
#               Inertia Stabilizers
from customEffects import boost
import model.fitting
def agilityMultiplierEffect(self, fitting, state):
    if state > model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "agility", "agilityMultiplier", self.item,
              useStackingPenalty = True)
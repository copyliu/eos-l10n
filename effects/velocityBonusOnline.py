#Used by: Item: Nanofiber Internal Structure
#               Overdrive Injector System
import model.fitting
from customEffects import boost
def velocityBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item,
              useStackingPenalty = True)
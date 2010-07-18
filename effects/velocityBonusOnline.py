#Items from group: Nanofiber Internal Structure (14 of 14) [Module]
#Items from group: Overdrive Injector System (14 of 14) [Module]
import model.fitting
from customEffects import boost
def velocityBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item,
              useStackingPenalty = True)
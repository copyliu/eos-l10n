#Used by: Afterburners, MicroWarpdrives
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfSpeedBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "speedFactor", "overloadSpeedFactorBonus", self.item)
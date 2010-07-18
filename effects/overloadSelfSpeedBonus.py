#Items from group: Afterburner (107 of 107)
from customEffects import boost
import model.fitting
type = "overload"
def overloadSelfSpeedBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "speedFactor", "overloadSpeedFactorBonus", self.item)
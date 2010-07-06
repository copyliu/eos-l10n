#Used by: Item: Warp Disruptor
from customEffects import increase
import model.fitting
type = ("projected", "active")
def warpScramble(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE  and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        increase(fitting.ship, "warpScrambleStatus", "warpScrambleStrength", self.item)
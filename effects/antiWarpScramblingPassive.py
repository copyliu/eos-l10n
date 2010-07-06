#Used by: Item: Warp Core Stabilizer
from customEffects import increase
import model.fitting
def antiWarpScramblingPassive(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "warpScrambleStatus", "warpScrambleStrength", self.item)
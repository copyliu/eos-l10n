#Items from group: Signal Amplifier (11 of 11) [Module]
from customEffects import boost
import model.fitting

def shipMaxLockedTargetsBonusAddOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxLockedTargets", "maxLockedTargetsBonus", self.item)

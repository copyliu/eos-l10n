#Used by: Item: Signal Amplifier
from customEffects import boost
import model.fitting

def shipMaxLockedTargetsBonusAddOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxLockedTargets", "maxLockedTargetsBonus", self.item)

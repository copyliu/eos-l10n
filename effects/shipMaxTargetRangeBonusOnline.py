#Used by: Item: Signal Amplifier
from customEffects import boost
import model.fitting

def shipMaxTargetRangeBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, useStackingPenalty = True)

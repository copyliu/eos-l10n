#Used by: Item: Remote Sensor Dampener
import model.fitting
from customEffects import boost
type = ("projected", "active")
def targetMaxTargetRangeAndScanResolutionBonusHostile(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanResolution", "scanResolutionBonus",
              self.item, useStackingPenalty = True)
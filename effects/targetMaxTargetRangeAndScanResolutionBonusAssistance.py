#Used by: Item: Remote Sensor Booster
import model.fitting
from customEffects import boost
type = ("projected", "active")
def targetMaxTargetRangeAndScanResolutionBonusAssistance(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanResolution", "scanResolutionBonus",
              self.item, useStackingPenalty = True)
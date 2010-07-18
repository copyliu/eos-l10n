#Items from group: Sensor Booster (12 of 12) [Module]
from customEffects import boost
import model.fitting
type = "active"
def sensorBoosterActivePercentage(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanResolution", "scanResolutionBonus",
              self.item, useStackingPenalty = True)
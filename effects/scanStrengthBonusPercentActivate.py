#Items from group: ECCM (44 of 44)
import model.fitting
from customEffects import boost
type = "active"
def scanStrengthBonusPercentActivate(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        for scannerType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
            boost(fitting.ship, "scan" + scannerType + "Strength",
                  "scan" + scannerType + "StrengthPercent",
                  self.item, useStackingPenalty = True)

#Items from group: Sensor Backup Array (72 of 72) [Module]
import model.fitting
from customEffects import boost

def scanStrengthBonusPercentOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        for scannerType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
            boost(fitting.ship, "scan" + scannerType + "Strength",
                  "scan" + scannerType + "StrengthPercent",
                  self.item, useStackingPenalty = True)

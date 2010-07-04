#Used by: Item: ECM
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfECMStrenghtBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        for scannerType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
            boost(self.item, "scan" + scannerType + "StrengthBonus",
                  "overloadECMStrengthBonus", self.item, useStackingPenalty = True)

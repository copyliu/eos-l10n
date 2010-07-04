#Used by: Item: ECCM
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfECCMStrenghtBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        for scannerType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
            boost(self.item, "scan" + scannerType + "StrengthPercent",
                  "overloadECCMStrenghtBonus", self.item)

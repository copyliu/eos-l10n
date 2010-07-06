#Used by: Skill: Astrometrics Pinpointer
#         Item : Hardwiring - 'Prospector' PPF-X
from customEffects import boostAmmoListByReq
def baseMaxScanDeviationModifierRequiringAstrometrics(self, fitting, level = 1):
    boostAmmoListByReq(fitting.modules, "baseMaxScanDeviation", "maxScanDeviationModifier",
                       lambda skill: skill.name == "Astrometrics",
                       self.item, extraMult = level)
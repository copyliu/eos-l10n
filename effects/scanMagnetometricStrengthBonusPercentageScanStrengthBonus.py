#Items from group: ECM Stabilizer (6 of 6) [Module]
from customEffects import boostModListByReq
import model.fitting

def scanMagnetometricStrengthBonusPercentageScanStrengthBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(
            fitting.modules,
            "scanMagnetometricStrengthBonus",
            "scanStrengthBonus",
            lambda mod: mod.group.name == "ECM",
            self.item, useStackingPenalty = True
        )

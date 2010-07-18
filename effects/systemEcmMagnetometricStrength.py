#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemEcmMagnetometricStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "scanMagnetometricStrengthBonus", "scanMagnetometricStrengthMultiplier",
                      lambda mod: mod.group.name == "ECM",
                      self.item, helper = multiply)
#Used by: Item: Magnetar Effect Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemEcmMagnetometricStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "scanMagnetometricStrengthBonus", "scanMagnetometricStrengthMultiplier",
                      lambda mod: mod.group.name == "ECM",
                      self.item, helper = multiply)
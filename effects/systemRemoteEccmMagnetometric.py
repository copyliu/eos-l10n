#Used by: Item: Magnetar Effect Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemRemoteEccmMagnetometric(self, fitting, state):
    boostModListByReq(fitting.modules, "scanMagnetometricStrengthBonus", "scanMagnetometricStrengthMultiplier",
                      lambda mod: mod.group.name == "ECCM",
                      self.item, helper = multiply)
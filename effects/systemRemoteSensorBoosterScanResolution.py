#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListByReq, multiply
type = "projected"
def systemRemoteSensorBoosterScanResolution(self, fitting, state):
    boostModListByReq(fitting.modules, "scanResolutionBonus", "scanResolutionBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Booster",
                      self.item, helper = multiply)
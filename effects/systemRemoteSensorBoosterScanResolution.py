#Items from group: Effect Beacon (6 of 38)
from customEffects import boostModListByReq, multiply
type = "projected"
def systemRemoteSensorBoosterScanResolution(self, fitting, state):
    boostModListByReq(fitting.modules, "scanResolutionBonus", "scanResolutionBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Booster",
                      self.item, helper = multiply)
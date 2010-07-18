#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostModListByReq, multiply
type = "projected"
def systemSensorDampenerScanResolution(self, fitting, state):
    boostModListByReq(fitting.modules, "scanResolutionBonus", "scanResolutionBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, helper = multiply)
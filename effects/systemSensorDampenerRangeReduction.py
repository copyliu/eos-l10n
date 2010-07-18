#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import multiply, boostModListByReq
type = "projected"
def systemSensorDampenerRangeReduction(self, fitting, state):
    boostModListByReq(fitting.modules, "maxTargetRangeBonus", "maxTargetRangeBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, helper = multiply)

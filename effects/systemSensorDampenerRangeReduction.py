#Used by: Item: Magnetar Effect Beacon
from customEffects import multiply, boostModListByReq
type = "projected"
def systemSensorDampenerRangeReduction(self, fitting, state):
    boostModListByReq(fitting.modules, "maxTargetRangeBonus", "maxTargetRangeBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, helper = multiply)

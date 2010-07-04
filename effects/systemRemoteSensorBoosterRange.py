#Used by: Item: Magnetar Effect Beacon
from customEffects import multiply, boostModListByReq
type= "projected"
def systemRemoteSensorBoosterRange(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Booster",
                      self.item, helper = multiply)
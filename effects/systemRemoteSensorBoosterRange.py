#Items from group: Effect Beacon (6 of 38)
from customEffects import multiply, boostModListByReq
type= "projected"
def systemRemoteSensorBoosterRange(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonusMultiplier",
                      lambda mod: mod.group.name == "Remote Sensor Booster",
                      self.item, helper = multiply)
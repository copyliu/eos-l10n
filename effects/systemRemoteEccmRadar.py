#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemRemoteEccmRadar(self, fitting, state):
    boostModListByReq(fitting.modules, "scanRadarStrengthBonus", "scanRadarStrengthMultiplier",
                      lambda mod: mod.group.name == "ECCM",
                      self.item, helper = multiply)
#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemRemoteEccmGrav(self, fitting, state):
    boostModListByReq(fitting.modules, "scanGravimetricStrengthBonus", "scanGravimetricStrengthMultiplier",
                      lambda mod: mod.group.name == "ECCM",
                      self.item, helper = multiply)
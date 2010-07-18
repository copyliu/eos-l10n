#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadSelfDuration(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadSelfDurationBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadSelfDurationBonus" in mod.attributes,
                      self.item, helper = multiply)
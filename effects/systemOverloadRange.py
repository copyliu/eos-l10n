#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadRange(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadRangeBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadRangeBonus" in mod.attributes,
                      self.item, helper = multiply)
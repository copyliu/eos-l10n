#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadDurationBonus(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadSelfDurationBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadSelfDurationBonus" in mod.attributes,
                      self.item, helper = multiply)
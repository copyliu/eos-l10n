#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadHardening(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadHardeningBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadHardeningBonus" in mod.attributes,
                      self.item, helper = multiply)
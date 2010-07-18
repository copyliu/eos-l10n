#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadShieldBonus(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadShieldBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadShieldBonus" in mod.attributes,
                      self.item, helper = multiply)
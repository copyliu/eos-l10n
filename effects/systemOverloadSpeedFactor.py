#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadSpeedFactor(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadSpeedFactorBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadSpeedFactorBonus" in mod.attributes,
                      self.item, helper = multiply)
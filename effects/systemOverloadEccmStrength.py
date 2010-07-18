#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadEccmStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadECCMStrenghtBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadECCMStrenghtBonus" in mod.attributes,
                      self.item, helper = multiply)
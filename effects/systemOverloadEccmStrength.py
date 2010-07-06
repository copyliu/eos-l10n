#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadEccmStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadECCMStrenghtBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadECCMStrenghtBonus" in mod.attributes,
                      self.item, helper = multiply)
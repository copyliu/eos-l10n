#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadEcmStrength(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadECMStrenghtBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadECMStrenghtBonus" in mod.attributes,
                      self.item, helper = multiply)
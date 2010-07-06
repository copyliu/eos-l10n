#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadDurationBonus(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadSelfDurationBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadSelfDurationBonus" in mod.attributes,
                      self.item, helper = multiply)
#Used by: Item: Red Giant Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadRof(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadRofBonus", "overloadBonusMultiplier",
                      lambda mod: "overloadRofBonus" in mod.attributes,
                      self.item, helper = multiply)
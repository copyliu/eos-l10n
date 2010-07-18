#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadDamageModifier(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadDamageModifier", "overloadBonusMultiplier",
                      lambda mod: "overloadDamageModifier" in mod.attributes,
                      self.item, helper = multiply)
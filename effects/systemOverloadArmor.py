#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import boostModListByReq, multiply
def systemOverloadArmor(self, fitting, state):
    boostModListByReq(fitting.modules, "overloadArmorDamageAmount", "overloadBonusMultiplier",
                      lambda mod: "overloadArmorDamageAmount" in mod.attributes,
                      self.item, helper = multiply)
#Item: Small Blaster Specialization
from customEffects import boostModListByReq
def selfT2SmallHybridBlasterDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
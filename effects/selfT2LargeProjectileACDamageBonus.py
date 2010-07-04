#Used by: Skill: Large Autocannon Specialization
from customEffects import boostModListByReq
def selfT2LargeProjectileACDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
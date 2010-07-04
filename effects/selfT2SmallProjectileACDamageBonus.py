#Used by: Skill: Small Autocannon Specialization
from customEffects import boostModListByReq
def selfT2SmallProjectileACDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
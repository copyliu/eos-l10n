#Used by: Skill: Large Artillery Specialization
from customEffects import boostModListByReq
def selfT2LargeProjectileArtyDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
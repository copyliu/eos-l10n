#Used by: Skill: Medium Autocannon Specialization
from customEffects import boostModListByReq
def selfT2MediumProjectileACDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
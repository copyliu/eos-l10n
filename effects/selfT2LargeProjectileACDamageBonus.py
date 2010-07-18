#Item: Large Autocannon Specialization [Skill]
from customEffects import boostModListByReq
def selfT2LargeProjectileACDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
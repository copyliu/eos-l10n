#Item: Medium Autocannon Specialization [Skill]
from customEffects import boostModListByReq
def selfT2MediumProjectileACDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
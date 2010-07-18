#Item: Medium Artillery Specialization [Skill]
from customEffects import boostModListByReq
def selfT2MediumProjectileArtyDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
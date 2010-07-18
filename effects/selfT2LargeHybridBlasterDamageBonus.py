#Item: Large Blaster Specialization [Skill]
from customEffects import boostModListByReq
def selfT2LargeHybridBlasterDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
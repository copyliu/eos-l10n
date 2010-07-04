#Used by: Skill: Large Railgun Specialization
from customEffects import boostModListByReq
def selfT2LargeHybridRailDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
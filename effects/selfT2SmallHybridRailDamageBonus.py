#Used by: Skill: Small Railgun Specialization
from customEffects import boostModListByReq
def selfT2SmallHybridRailDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
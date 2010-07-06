#Used by: Skill: Small Beam Laser Specialization
from customEffects import boostModListByReq
def selfT2SmallLaserBeamDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
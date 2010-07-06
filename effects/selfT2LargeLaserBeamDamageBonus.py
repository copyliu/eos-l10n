#Used by: Skill: Large Beam Laser Specialization
from customEffects import boostModListByReq
def selfT2LargeLaserBeamDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
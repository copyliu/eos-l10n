#Used by: Skill: Medium Pulse Laser Specialization
from customEffects import boostModListByReq
def selfT2MediumLaserPulseDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
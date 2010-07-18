#Item: Large Pulse Laser Specialization [Skill]
from customEffects import boostModListByReq
def selfT2LargeLaserPulseDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
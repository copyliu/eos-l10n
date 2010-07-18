#Item: Capital Energy Turret
from customEffects import boostModListByReq
def capitalTurretSkillLaserDamage(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
#Used by: Skill: Capital Projectile Turret
from customEffects import boostModListByReq
def capitalTurretSkillProjectileDamage(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
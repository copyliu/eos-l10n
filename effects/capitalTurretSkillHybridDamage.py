#Item: Capital Hybrid Turret [Skill]
from customEffects import boostModListByReq
def capitalTurretSkillHybridDamage(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)
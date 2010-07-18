#Item: Loki Offensive - Turret Concurrence Registry [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensive2ProjectileWeaponDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "subsystemBonusMinmatarOffensive2",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
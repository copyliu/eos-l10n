#Item: Loki Offensive - Turret Concurrence Registry [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensiveProjectileWeaponMaxRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "maxRange", "subsystemBonusMinmatarOffensive",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
#Item: Loki Offensive - Projectile Scoping Array
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensiveProjectileWeaponFalloff(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "falloff", "subsystemBonusMinmatarOffensive",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
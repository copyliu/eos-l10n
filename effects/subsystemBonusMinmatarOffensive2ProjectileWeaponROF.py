#Used by: Item: Loki Offensive - Projectile Scoping Array
#               Hardpoint Efficiency Configuration
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensive2ProjectileWeaponROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "speed", "subsystemBonusMinmatarOffensive2",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
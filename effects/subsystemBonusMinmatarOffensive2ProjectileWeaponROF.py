#Variations of item: Loki Offensive - Turret Concurrence Registry (2 of 4)
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensive2ProjectileWeaponROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "speed", "subsystemBonusMinmatarOffensive2",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
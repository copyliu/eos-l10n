#Used by: Item: Loki Defensive - Covert Reconfiguration
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensiveProjectileWeaponROF(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "speed", "subsystemBonusMinmatarOffensive",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
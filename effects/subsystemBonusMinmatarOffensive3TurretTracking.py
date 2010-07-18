#Item: Loki Offensive - Turret Concurrence Registry
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarOffensive3TurretTracking(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Offensive Systems")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "subsystemBonusMinmatarOffensive3",
                      lambda skill: skill.name == "Medium Projectile Turret",
                      self.item, extraMult = level)
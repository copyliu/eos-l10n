#Used by: Ship: Sabre
from customEffects import boostModListBySkillReq
def eliteBonusInterdictorsProjectileFalloff1(self, fitting):
    skill, level = fitting.getCharSkill("Interdictors")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusInterdictors1",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
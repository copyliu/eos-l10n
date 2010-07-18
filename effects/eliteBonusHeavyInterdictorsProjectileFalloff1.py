#Item: Broadsword [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyInterdictorsProjectileFalloff1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Interdictors")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusHeavyInterdictors1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
#Item: Phobos
from customEffects import boostModListBySkillReq
def eliteBonusHeavyInterdictorsHybridFalloff1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Interdictors")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusHeavyInterdictors1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
#Used by: Ship: Devoter
from customEffects import boostModListBySkillReq
def eliteBonusHeavyInterdictorLaserRof(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Interdictors")
    boostModListBySkillReq(fitting.modules, "speed", "eliteBonusHeavyInterdictors1",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
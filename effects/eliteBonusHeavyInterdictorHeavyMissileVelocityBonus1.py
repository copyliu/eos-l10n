#Used by: Ship: Onyx
from customEffects import boostAmmoListBySkillReq
def eliteBonusHeavyInterdictorHeavyMissileVelocityBonus1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Interdictors")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusHeavyInterdictors1",
                       lambda skill: skill.name == "Heavy Missiles",
                       self.item, extraMult = level)
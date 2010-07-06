#Used by: Ship: Eagle
#               Deimos
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipHybridDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusHeavyGunship2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
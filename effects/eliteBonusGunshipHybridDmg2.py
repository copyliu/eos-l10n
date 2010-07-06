#Used by: Ship: Harpy
from customEffects import boostModListBySkillReq
def eliteBonusGunshipHybridDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusGunship2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)

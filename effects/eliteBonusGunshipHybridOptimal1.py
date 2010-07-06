#Used by: Ship: Harpy
#               Ishkur
#               Enyo
from customEffects import boostModListBySkillReq
def eliteBonusGunshipHybridOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusGunship1",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
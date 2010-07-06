#Used by: Ship: Catalyst
from customEffects import boostModListBySkillReq
def shipHybridFallOffGD1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusDF1",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
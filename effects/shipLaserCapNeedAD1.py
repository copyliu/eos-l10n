#Used by: Ship: Coercer
from customEffects import boostModListBySkillReq
def shipLaserCapNeedAD1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusDF1",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
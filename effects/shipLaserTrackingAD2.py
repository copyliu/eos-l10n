#Used by: Ship: Coercer
from customEffects import boostModListBySkillReq
def shipLaserTrackingAD2(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusDF2",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
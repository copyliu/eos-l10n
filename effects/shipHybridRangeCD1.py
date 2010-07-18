#Item: Cormorant
from customEffects import boostModListBySkillReq
def shipHybridRangeCD1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusDF1",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
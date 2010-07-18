#Variations of item: Catalyst (2 of 2) [Ship]
#Item: Cormorant [Ship]
from customEffects import boostModListBySkillReq
def shipHybridTrackingGD2(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusDF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
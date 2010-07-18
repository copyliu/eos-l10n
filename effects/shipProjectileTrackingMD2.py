#Variations of item: Thrasher (2 of 2)
from customEffects import boostModListBySkillReq
def shipProjectileTrackingMD2(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusDF2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
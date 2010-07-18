#Variations of item: Thrasher (2 of 2)
from customEffects import boostModListBySkillReq
def shipProjectileDamageDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusDF1",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
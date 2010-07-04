#Used by: Ship: Heretic
from customEffects import boostAmmoListBySkillReq
def shipRocketEmDmgDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusDF1",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
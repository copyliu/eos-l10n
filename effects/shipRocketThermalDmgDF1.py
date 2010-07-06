#Used by: Ship: Heretic
from customEffects import boostAmmoListBySkillReq
def shipRocketThermalDmgDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusDF1",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
#Item: Heretic
from customEffects import boostAmmoListBySkillReq
def shipRocketKineticDmgDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusDF1",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
#Item: Heretic [Ship]
from customEffects import boostAmmoListBySkillReq
def shipRocketExplosiveDmgDF1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusDF1",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
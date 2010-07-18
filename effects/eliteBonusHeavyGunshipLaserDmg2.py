#Item: Zealot [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipLaserDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusHeavyGunship2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
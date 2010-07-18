#Item: Zealot [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipLaserOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusHeavyGunship1",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
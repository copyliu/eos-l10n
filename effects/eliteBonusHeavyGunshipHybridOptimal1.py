#Item: Eagle [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipHybridOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusHeavyGunship1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
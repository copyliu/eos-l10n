#Item: Deimos
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipHybridFallOff1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusHeavyGunship1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
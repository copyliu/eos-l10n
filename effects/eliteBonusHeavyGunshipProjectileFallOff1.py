#Item: Vagabond [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipProjectileFallOff1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusHeavyGunship1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
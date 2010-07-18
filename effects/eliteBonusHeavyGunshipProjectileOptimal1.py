#Item: Muninn [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipProjectileOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusHeavyGunship1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
#Item: Muninn
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipProjectileTracking2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusHeavyGunship2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
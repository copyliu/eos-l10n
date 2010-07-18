#Item: Wolf [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusGunshipProjectileDamage1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusGunship1",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
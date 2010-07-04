#Used by: Ship: Vagabond
from customEffects import boostModListBySkillReq
def eliteBonusHeavyGunshipProjectileDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusHeavyGunship2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
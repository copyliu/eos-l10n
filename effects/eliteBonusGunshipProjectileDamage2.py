#Used by: Ship: Jaguar
from customEffects import boostModListBySkillReq
def eliteBonusGunshipProjectileDamage2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusGunship2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
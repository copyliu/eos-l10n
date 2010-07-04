#Used by: Ship: Wolf
from customEffects import boostModListBySkillReq
def eliteBonusGunshipProjectileFalloff2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusGunship2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
    

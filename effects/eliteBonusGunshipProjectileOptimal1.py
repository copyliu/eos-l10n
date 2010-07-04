#Used by: Ship: Jaguar
from customEffects import boostModListBySkillReq
def eliteBonusGunshipProjectileOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusGunship1",
                      lambda skill: skill.name == "Small Projectile Turret",
                      self.item, extraMult = level)
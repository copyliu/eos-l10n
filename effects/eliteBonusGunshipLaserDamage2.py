#Used by: Ship: Retribution
from customEffects import boostModListBySkillReq
def eliteBonusGunshipLaserDamage2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusGunship2",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
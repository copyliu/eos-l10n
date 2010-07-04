#Used by: Ship: Cerberus
from customEffects import boostAmmoListBySkillReq
def eliteBonusHeavyGunshipAssaultMissileFlightTime1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "eliteBonusHeavyGunship1",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)
#Item: Cerberus
from customEffects import boostAmmoListBySkillReq
def eliteBonusHeavyGunshipHeavyMissileFlightTime1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "eliteBonusHeavyGunship1",
                       lambda skill: skill.name == "Heavy Missiles",
                       self.item, extraMult = level)
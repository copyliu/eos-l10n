#Item: Legion Offensive - Assault Optimization [Subsystem]
from customEffects import boostAmmoListBySkillReq
def subsystemBonusAmarrOffensive2HAMExplosiveDamage(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "subsystemBonusAmarrOffensive2",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)
#Item: Legion Offensive - Assault Optimization [Subsystem]
from customEffects import boostAmmoListBySkillReq
def subsystemBonusAmarrOffensive2HAMThermalDamage(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "subsystemBonusAmarrOffensive2",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item, extraMult = level)
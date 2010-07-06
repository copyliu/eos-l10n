#Used by: Ship: Vengeance
#               Malediction
#               Anathema
from customEffects import boostAmmoListBySkillReq
def shipRocketThermalDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
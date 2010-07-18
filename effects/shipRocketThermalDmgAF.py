#Item: Anathema [Ship]
#Item: Malediction [Ship]
#Item: Vengeance [Ship]
from customEffects import boostAmmoListBySkillReq
def shipRocketThermalDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
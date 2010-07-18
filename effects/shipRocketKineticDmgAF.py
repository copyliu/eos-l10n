#Item: Anathema
#Item: Malediction
#Item: Vengeance
from customEffects import boostAmmoListBySkillReq
def shipRocketKineticDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
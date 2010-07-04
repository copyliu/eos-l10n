#Used by: Ship: Vengeance
#               Malediction
#               Anathema
from customEffects import boostAmmoListBySkillReq
def shipRocketEmDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
#Used by: Ship: Vengeance
#               Malediction
#               Anathema
from customEffects import boostAmmoListBySkillReq
def shipRocketExplosiveDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
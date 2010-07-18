#Item: Anathema [Ship]
#Item: Malediction [Ship]
#Item: Vengeance [Ship]
from customEffects import boostAmmoListBySkillReq
def shipRocketExplosiveDmgAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "shipBonusAF",
                       lambda skill: skill.name == "Rockets",
                       self.item, extraMult = level)
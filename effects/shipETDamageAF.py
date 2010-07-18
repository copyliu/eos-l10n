#Item: Crusader
#Item: Imperial Navy Slicer
from customEffects import boostModListBySkillReq
def shipETDamageAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusAF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)

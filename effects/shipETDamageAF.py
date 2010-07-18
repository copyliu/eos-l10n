#Item: Crusader [Ship]
#Item: Imperial Navy Slicer [Ship]
from customEffects import boostModListBySkillReq
def shipETDamageAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusAF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)

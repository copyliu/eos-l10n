#Item: Executioner [Ship]
#Item: Gold Magnate [Ship]
#Item: Silver Magnate [Ship]
from customEffects import boostModListBySkillReq
def shipSETDmgBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusAF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
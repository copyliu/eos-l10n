#Used by: Ship: Executioner
#               Silver Magnate
#               Gold Magnate
from customEffects import boostModListBySkillReq
def shipSETDmgBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusAF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
#Used by: Ship: Omen
#               Omen Navy Issue
#               Zealot
from customEffects import boostModListBySkillReq
def shipLaserRofAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusAC2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)

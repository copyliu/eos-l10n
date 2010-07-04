#Used by: Ship: Augoror Navy Issue
#               Maller
#               Omen
#               Omen Navy Issue
#               Devoter
#               Zealot
from customEffects import boostModListBySkillReq
def shipTCapNeedBonusAC(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusAC",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)

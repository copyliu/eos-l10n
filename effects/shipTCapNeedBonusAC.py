#Variations of item: Omen (3 of 3)
#Item: Augoror Navy Issue
#Item: Devoter
#Item: Maller
from customEffects import boostModListBySkillReq
def shipTCapNeedBonusAC(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusAC",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)

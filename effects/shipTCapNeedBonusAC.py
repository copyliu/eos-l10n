#Variations of item: Maller (2 of 3) [Ship]
#Variations of item: Omen (3 of 3) [Ship]
#Item: Augoror Navy Issue [Ship]
from customEffects import boostModListBySkillReq
def shipTCapNeedBonusAC(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusAC",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)

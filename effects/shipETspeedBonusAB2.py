#Variations of item: Armageddon (4 of 5)
from customEffects import boostModListBySkillReq
def shipETspeedBonusAB2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusAB2",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)

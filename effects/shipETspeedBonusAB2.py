#Used by: Ship: Armageddon
#               Armageddon Navy Issue
#               Armageddon Imperial Issue
#               Redeemer
from customEffects import boostModListBySkillReq
def shipETspeedBonusAB2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusAB2",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)

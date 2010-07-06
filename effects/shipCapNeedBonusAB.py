#Used by: Ship: Armageddon
#               Armageddon Navy Issue
#               Armageddon Imperial Issue
#               Apocalypse
#               Apocalypse Navy Issue
#               Apocalypse Imperial Issue
#               Redeemer
from customEffects import boostModListBySkillReq
def shipCapNeedBonusAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusAB",
                      lambda skill: skill.name == "Large Energy Turret",
                      self.item, extraMult = level)

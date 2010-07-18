#Variations of item: Apocalypse (3 of 4) [Ship]
#Variations of item: Armageddon (4 of 5) [Ship]
from customEffects import boostModListBySkillReq
def shipCapNeedBonusAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonusAB",
                      lambda skill: skill.name == "Large Energy Turret",
                      self.item, extraMult = level)

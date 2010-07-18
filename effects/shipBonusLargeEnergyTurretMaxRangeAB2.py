#Variations of item: Apocalypse (2 of 4)
from customEffects import boostModListBySkillReq
def shipBonusLargeEnergyTurretMaxRangeAB2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusAB2",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)

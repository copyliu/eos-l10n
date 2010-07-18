#Item: Apocalypse [Ship]
#Item: Apocalypse Navy Issue [Ship]
from customEffects import boostModListBySkillReq
def shipBonusLargeEnergyTurretMaxRangeAB2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusAB2",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)

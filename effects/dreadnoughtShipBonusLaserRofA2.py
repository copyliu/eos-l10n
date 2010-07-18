#Item: Revelation [Ship]
from customEffects import boostModListBySkillReq
def dreadnoughtShipBonusLaserRofA2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Dreadnought")
    boostModListBySkillReq(fitting.modules, "speed", "dreadnoughtShipBonusA2",
                           lambda skill: skill.name == "Capital Energy Turret",
                           self.item, extraMult = level)
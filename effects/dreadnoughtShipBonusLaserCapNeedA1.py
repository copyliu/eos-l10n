#Item: Revelation
from customEffects import boostModListBySkillReq
def dreadnoughtShipBonusLaserCapNeedA1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Dreadnought")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "dreadnoughtShipBonusA1",
                           lambda skill: skill.name == "Capital Energy Turret",
                           self.item, extraMult = level)
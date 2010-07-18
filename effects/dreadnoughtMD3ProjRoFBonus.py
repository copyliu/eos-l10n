#Item: Naglfar
from customEffects import boostModListBySkillReq
def dreadnoughtMD3ProjRoFBonus(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Dreadnought")
    boostModListBySkillReq(fitting.modules, "speed", "dreadnoughtShipBonusM3",
                           lambda skill: skill.name == "Capital Projectile Turret",
                           self.item, extraMult = level)

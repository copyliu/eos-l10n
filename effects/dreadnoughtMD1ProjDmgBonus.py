#Item: Naglfar
from customEffects import boostModListBySkillReq
def dreadnoughtMD1ProjDmgBonus(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Dreadnought")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "dreadnoughtShipBonusM1",
                           lambda skill: skill.name == "Capital Projectile Turret",
                           self.item, extraMult = level)

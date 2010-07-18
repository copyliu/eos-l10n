#Item: Moros
from customEffects import boostModListBySkillReq
def dreadnoughtShipBonusHybridDmgG1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Dreadnought")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "dreadnoughtShipBonusG1",
                           lambda skill: skill.name == "Capital Hybrid Turret",
                           self.item, extraMult = level)
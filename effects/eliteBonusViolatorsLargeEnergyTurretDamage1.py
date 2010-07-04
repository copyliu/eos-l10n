#Used by: Ship: Paladin
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeEnergyTurretDamage1(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusViolators1",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)
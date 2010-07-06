#Used by: Ship: Kronos
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeHybridTurretTracking1(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusViolators1",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
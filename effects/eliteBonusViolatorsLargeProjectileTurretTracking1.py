#Item: Vargur
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeProjectileTurretTracking1(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusViolators1",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
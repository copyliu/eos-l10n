#Used by: Skill: Large Hybrid Turret
from customEffects import boostModListBySkillReq
def largeHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
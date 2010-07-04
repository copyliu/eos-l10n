#Used by: Skill: Large Projectile Turret
from customEffects import boostModListBySkillReq
def largeProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
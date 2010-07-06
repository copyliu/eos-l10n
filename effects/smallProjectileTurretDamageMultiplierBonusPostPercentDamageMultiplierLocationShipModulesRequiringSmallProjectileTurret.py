#Used by: Skill: Small Projectile Turret
from customEffects import boostModListBySkillReq
def smallProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Projectile Turret", 
                           self.item, extraMult = level)
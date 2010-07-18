#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-2 [Implant]
#Item: Small Projectile Turret [Skill]
from customEffects import boostModListBySkillReq
def smallProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Projectile Turret", 
                           self.item, extraMult = level)
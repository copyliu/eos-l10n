#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-2 [Implant]
#Item: Large Projectile Turret [Skill]
from customEffects import boostModListBySkillReq
def largeProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
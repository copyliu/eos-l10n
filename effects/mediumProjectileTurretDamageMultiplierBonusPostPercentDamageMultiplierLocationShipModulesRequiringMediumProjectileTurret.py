#Item: Hardwiring - Eifyr and Co 'Gunslinger' MX-2 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' MX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' MX-1 [Implant]
#Item: Medium Projectile Turret [Skill]
from customEffects import boostModListBySkillReq
def mediumProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
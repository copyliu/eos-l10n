#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Gunnery Implants (3 of 12)
#Item: Large Projectile Turret [Skill]
from customEffects import boostModListBySkillReq
def largeProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Gunnery Implants (3 of 9)
#Item: Small Projectile Turret
from customEffects import boostModListBySkillReq
def smallProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Projectile Turret", 
                           self.item, extraMult = level)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Gunnery Implants (3 of 9)
#Item: Medium Projectile Turret
from customEffects import boostModListBySkillReq
def mediumProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Gunnery Implants (3 of 12)
#Item: Large Energy Turret
#Item: Pashan's Turret Handling Mindlink
from customEffects import boostModListBySkillReq
def largeEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)
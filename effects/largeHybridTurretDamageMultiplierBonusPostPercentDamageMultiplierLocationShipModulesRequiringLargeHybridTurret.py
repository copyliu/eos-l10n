#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Gunnery Implants (3 of 12)
#Item: Large Hybrid Turret
from customEffects import boostModListBySkillReq
def largeHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
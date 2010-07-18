#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Gunnery Implants (3 of 9)
#Item: Small Hybrid Turret
from customEffects import boostModListBySkillReq
def smallHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
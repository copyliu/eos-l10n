#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Gunnery Implants (3 of 9)
#Item: Small Energy Turret
from customEffects import boostModListBySkillReq
def smallEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
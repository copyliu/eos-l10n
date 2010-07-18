#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Gunnery Implants (3 of 9)
#Item: Medium Energy Turret [Skill]
from customEffects import boostModListBySkillReq
def mediumEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
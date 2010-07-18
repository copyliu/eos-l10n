#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Gunnery Implants (3 of 9)
#Item: Medium Hybrid Turret [Skill]
from customEffects import boostModListBySkillReq
def mediumHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
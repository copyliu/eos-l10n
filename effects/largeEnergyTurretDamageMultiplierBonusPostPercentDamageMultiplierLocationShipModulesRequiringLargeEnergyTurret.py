#Item: Hardwiring - Inherent Implants 'Lancer' G0-Epsilon [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Epsilon [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Epsilon [Implant]
#Item: Large Energy Turret [Skill]
#Item: Pashan's Turret Handling Mindlink [Implant]
from customEffects import boostModListBySkillReq
def largeEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)
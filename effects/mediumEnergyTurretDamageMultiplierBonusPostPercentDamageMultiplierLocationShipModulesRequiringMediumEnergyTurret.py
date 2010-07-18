#Item: Hardwiring - Inherent Implants 'Lancer' G0-Gamma [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Gamma [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Gamma [Implant]
#Item: Medium Energy Turret [Skill]
from customEffects import boostModListBySkillReq
def mediumEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
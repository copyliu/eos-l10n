#Item: Hardwiring - Inherent Implants 'Lancer' G0-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Alpha [Implant]
#Item: Small Energy Turret [Skill]
from customEffects import boostModListBySkillReq
def smallEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
#Used by: Skill: Small Energy Turret
from customEffects import boostModListBySkillReq
def smallEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
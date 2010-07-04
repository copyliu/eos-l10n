#Used by: Skill: Small Hybrid Turret
from customEffects import boostModListBySkillReq
def smallHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
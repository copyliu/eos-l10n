#Item: Hardwiring - Zainou 'Deadeye' ZGS10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGS100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGS1000 [Implant]
#Item: Small Hybrid Turret [Skill]
from customEffects import boostModListBySkillReq
def smallHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringSmallHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus", 
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
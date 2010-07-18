#Item: Hardwiring - Zainou 'Deadeye' ZGL10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGL100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGL1000 [Implant]
#Item: Large Hybrid Turret [Skill]
from customEffects import boostModListBySkillReq
def largeHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
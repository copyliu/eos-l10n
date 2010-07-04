#Used by: Skill: Large Energy Turret
from customEffects import boostModListBySkillReq
def largeEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringLargeEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)
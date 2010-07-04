#Used by: Skill: Medium Energy Turret
from customEffects import boostModListBySkillReq
def mediumEnergyTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumEnergyTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)
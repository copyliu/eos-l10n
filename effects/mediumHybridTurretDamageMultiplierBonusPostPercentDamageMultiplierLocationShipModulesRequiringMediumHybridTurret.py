#Used by: Skill: Medium Hybrid Turret
from customEffects import boostModListBySkillReq
def mediumHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
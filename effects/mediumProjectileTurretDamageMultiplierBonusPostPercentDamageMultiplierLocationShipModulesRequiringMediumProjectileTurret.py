#Used by: Skill: Medium Projectile Turret
from customEffects import boostModListBySkillReq
def mediumProjectileTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumProjectileTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
#Used by: Skill: Citadel Torpedoes
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelThermalDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Torpedoes",
                            self.item, extraMult = level)
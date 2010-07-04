#Used by: Skill: Citadel Torpedoes
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelKineticDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Citadel Torpedoes",
                       self.item, extraMult = level)
#Used by: Skill: Citadel Torpedoes
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelEmDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Citadel Torpedoes",
                       self.item, extraMult = level)
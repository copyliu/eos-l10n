#Used by: Skill: Citadel Torpedoes
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelExplosiveDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Citadel Torpedoes",
                       self.item, extraMult = level)
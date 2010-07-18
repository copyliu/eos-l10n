#Items from group: Cyber Missile (3 of 46) [Implant]
#Item: Citadel Torpedoes [Skill]
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelExplosiveDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Citadel Torpedoes",
                       self.item, extraMult = level)
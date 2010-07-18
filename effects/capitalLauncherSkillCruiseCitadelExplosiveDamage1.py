#Item: Citadel Cruise Missiles [Skill]
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCruiseCitadelExplosiveDamage1(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Cruise Missiles",
                            self.item, extraMult = level)

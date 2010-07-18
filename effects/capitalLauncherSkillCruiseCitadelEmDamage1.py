#Item: Citadel Cruise Missiles
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCruiseCitadelEmDamage1(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Cruise Missiles",
                            self.item, extraMult = level)

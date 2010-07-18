#Item: Citadel Cruise Missiles
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCruiseCitadelKineticDamage1(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Cruise Missiles",
                            self.item, extraMult = level)

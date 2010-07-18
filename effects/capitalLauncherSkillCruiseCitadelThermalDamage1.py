#Item: Citadel Cruise Missiles [Skill]
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCruiseCitadelThermalDamage1(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Cruise Missiles",
                            self.item, extraMult = level)

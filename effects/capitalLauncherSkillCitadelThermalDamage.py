#Item: Citadel Torpedoes [Skill]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX10 [Implant]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX100 [Implant]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX1000 [Implant]
from customEffects import boostAmmoListBySkillReq
def capitalLauncherSkillCitadelThermalDamage(self, fitting, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Citadel Torpedoes",
                            self.item, extraMult = level)
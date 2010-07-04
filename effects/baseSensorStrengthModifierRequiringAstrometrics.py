#Used by: Skill: Astrometrics Rangefinding 
#         Item : Virtue Implant Set
#                Hardwiring - 'Prospector' PPH-X
#                Sister Probe Launchers
#                Gravity Capacitor Upgrade
from customEffects import boostAmmoListBySkillReq
def baseSensorStrengthModifierRequiringAstrometrics(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "baseSensorStrength", "scanStrengthBonus",
                            lambda skill: skill.name == "Astrometrics",
                            self.item, extraMult = level)
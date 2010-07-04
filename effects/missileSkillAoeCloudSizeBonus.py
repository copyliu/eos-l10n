#Used by: Skill: Guided Missile Precision
#         Item : Crash Booster
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Standard Missiles" or \
                            skill.name == "Heavy Missiles" or \
                            skill.name == "Cruise Missiles",
                            self.item, extraMult = level)
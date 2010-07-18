#Item: Improved Crash Booster [Implant]
#Item: Standard Crash Booster [Implant]
#Item: Strong Crash Booster [Implant]
#Item: Synth Crash Booster [Implant]
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonusAll(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item)
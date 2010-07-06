#Used by: Item: Crash Booster
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonusAll(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item)
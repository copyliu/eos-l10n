#Used by: Item: Hardwiring 'Snapshot' ZMFX
from customEffects import boostAmmoListBySkillReq
def missileSkillFoFAoeCloudSizeBonus(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "FoF Missiles", self.item)
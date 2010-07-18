#Items from market group: Implants & Boosters > Booster (4 of 32)
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonusAll(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Missile Implants (3 of 6)
from customEffects import boostAmmoListBySkillReq
def missileSkillFoFAoeCloudSizeBonus(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "FoF Missiles", self.item)
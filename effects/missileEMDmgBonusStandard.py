#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)
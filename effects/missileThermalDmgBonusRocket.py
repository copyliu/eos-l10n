#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)
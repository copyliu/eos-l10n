#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)
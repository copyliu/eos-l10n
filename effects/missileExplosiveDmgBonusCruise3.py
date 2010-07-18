#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)
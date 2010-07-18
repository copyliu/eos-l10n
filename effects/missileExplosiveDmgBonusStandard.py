#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Missile Implants (3 of 9)
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)